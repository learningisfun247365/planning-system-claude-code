"""Morning Brief: daily AI + Learning industry briefing scanner.

Fetches RSS feeds and discovery search results, asks Claude to filter and
route items into editorial sections, renders the result as a static site and
optionally a markdown copy into an Obsidian vault.

Run modes:
  python scan.py                      # full run, writes docs/
  python scan.py --dry-run            # fetch + log only, no files
  python scan.py --write-vault \
      --vault-path /path/to/vault     # also write markdown to vault

Environment variables:
  ANTHROPIC_API_KEY (required for synthesis; falls back to raw links if unset)
  TAVILY_API_KEY    (optional; if unset, discovery queries are skipped)
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import logging
import os
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Optional

import feedparser
import yaml
from dateutil import parser as dateparser
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
REPO_ROOT = ROOT.parent
DOCS = REPO_ROOT / "docs"
BRIEFINGS = DOCS / "briefings"
TEMPLATES = ROOT / "templates"
SEEN_PATH = ROOT / "seen.json"
SOURCES_PATH = ROOT / "sources.yml"
SYNTHESIS_MODEL = "claude-sonnet-4-6"
MAX_SEEN_ENTRIES = 8000
MAX_ITEMS_PER_FEED = 40
MAX_CANDIDATES_TO_SYNTHESIZE = 120

SECTION_ORDER = [
    "Plumbing",
    "New Modes of Doing",
    "ID Craft",
    "Org & Talent Design",
    "Steering & Judgment",
    "Cross-Pollination",
    "Cool & Weird",
]

EDITORIAL_SYSTEM_PROMPT = """You are the editor of a daily briefing called "Morning Brief" for a constructivist-humanist instructional designer who works on workforce/adult learning (NOT K-12). She is technical-non-technical: comfortable with concepts, curious about mechanism, but not a working engineer.

Her actual toolset: Pi (harness), Codex app, Claude Code (terminal), Claude Desktop with cowork. She does NOT use Cursor, Copilot, or Windsurf.

EDITORIAL FOCUS — what she cares about:
- AI-native, AI-pilled companies doing radically new things (not legacy L&D vendors)
- Completely new ways of getting employees what they need to know when they need it
- Instructional design as a CRAFT — the full build cycle, design-thinking-for-L&D style
- How AI-native orgs are restructuring workforce, roles, skill ladders
- Technical plumbing: memory, agents, context engineering, MCP, evals, parallel agents
- The new learning niche: critical thinking, judgment, evaluation, steering parallel work
- Cross-pollination — borrowings from other fields (cog sci, design, neuroscience, complexity) applied to learning
- The cool, weird, outliers — building-in-public artifacts (Karpathy wiki LLM is canonical)

PROMOTE:
- AI-native practitioners and companies doing things differently
- Posts explaining HOW the plumbing actually works
- Building-in-public artifacts and novel experiments
- ID-craft writing on mechanics (action mapping, scenario design, evidence-based ID)
- Org/talent pieces that name SPECIFIC structural changes
- Pieces that imply a learning move — "what new doing this enables", "what judgment is now needed"
- Cross-field borrowings
- Epistemic counterweight — critique that names specific failure modes

DEMOTE / SPIKE:
- Generic "AI is transforming learning!" thought-leadership puff
- LinkedIn Learning / Cornerstone / Docebo product announcements
- K-12 ed-tech (her work is workforce/adult)
- "5 ways AI will change L&D" listicles
- Vendor case studies that don't reveal mechanism
- Big-consulting "future of work" pieces with no specific structural claim
- Cursor / Copilot / Windsurf tool launches unless they reveal a broader pattern
- Pure tech news without a learning-relevant angle

SECTIONS (route each kept item into exactly one; create no other sections):
1. "Plumbing" — memory, agents, context, RAG, MCP, evals, multi-agent orchestration, interpretability
2. "New Modes of Doing" — AI-native ways of getting people what they need to know when they need it; agentic workflows in actual companies
3. "ID Craft" — instructional design mechanics, the build cycle, evidence-based practice
4. "Org & Talent Design" — how AI-native orgs restructure workforce, roles, skill ladders, team shapes
5. "Steering & Judgment" — critical thinking, evals, prompt/agent steering, parallel-tracks, epistemic skepticism
6. "Cross-Pollination" — other fields applied to learning
7. "Cool & Weird" — outliers, building-in-public, off-beat experiments

OUTPUT — for each KEPT item write a one-sentence TAKE (not a summary):
- What's new or strange about this, and what it implies for learning design or learner judgment.
- Avoid the words "great", "insightful", "important", "must-read". Be specific.

SPECIAL RULE — for ANY item routed into "Plumbing", also write a "plain_take" — one sentence explaining the technical concept in non-engineer terms. Assume the reader is conceptually curious but not a working engineer. NO code in plain_take.

Also write a one-sentence "summary" for the top of the page — what is the day's signal? If items are sparse, say so.

Items you SPIKE: include in the spiked list with a short spiked_reason ("vendor PR", "K-12", "tool launch — not her stack", etc).

Return STRICT JSON only — no prose before or after, no markdown fences — matching this schema:

{
  "summary": "one sentence day-signal",
  "sections": {
    "Plumbing": [
      {"i": <int>, "take": "...", "plain_take": "..."},
      ...
    ],
    "New Modes of Doing": [ {"i": <int>, "take": "..."}, ... ],
    "ID Craft": [...],
    "Org & Talent Design": [...],
    "Steering & Judgment": [...],
    "Cross-Pollination": [...],
    "Cool & Weird": [...]
  },
  "spiked": [
    {"i": <int>, "spiked_reason": "..."},
    ...
  ]
}

Use the original integer `i` index from the candidate items. Omit empty sections (drop the key). Do NOT invent items not in the candidate list."""


@dataclass
class Item:
    title: str
    url: str
    source: str
    source_category: str = "uncategorized"
    published: Optional[str] = None
    summary: str = ""
    section: Optional[str] = None
    take: Optional[str] = None
    plain_take: Optional[str] = None
    spiked_reason: Optional[str] = None


# ---------------------------------------------------------------------------
# IO helpers
# ---------------------------------------------------------------------------

def load_seen() -> dict[str, int]:
    if SEEN_PATH.exists():
        try:
            return json.loads(SEEN_PATH.read_text())
        except json.JSONDecodeError:
            logging.warning("seen.json was corrupt; starting fresh")
    return {}


def save_seen(seen: dict[str, int]) -> None:
    pruned = dict(sorted(seen.items(), key=lambda kv: kv[1], reverse=True)[:MAX_SEEN_ENTRIES])
    SEEN_PATH.write_text(json.dumps(pruned, indent=2, sort_keys=True))


def url_key(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Fetchers
# ---------------------------------------------------------------------------

def _strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def fetch_rss(source: dict, since: dt.datetime) -> list[Item]:
    name = source["name"]
    url = source["url"]
    category = source.get("category", "uncategorized")
    out: list[Item] = []
    try:
        feed = feedparser.parse(url)
    except Exception as exc:
        logging.warning("  ! %s: parse error: %s", name, exc)
        return out

    if getattr(feed, "bozo", False) and not feed.entries:
        logging.warning("  ! %s: feed unreadable (%s)", name, getattr(feed, "bozo_exception", "unknown"))
        return out

    for entry in feed.entries[:MAX_ITEMS_PER_FEED]:
        published: Optional[dt.datetime] = None
        for key in ("published", "updated", "created"):
            value = entry.get(key)
            if not value:
                continue
            try:
                published = dateparser.parse(value)
                break
            except (ValueError, TypeError, OverflowError):
                continue

        if published is not None:
            published_utc = published.astimezone(dt.timezone.utc) if published.tzinfo else published.replace(tzinfo=dt.timezone.utc)
            if published_utc < since:
                continue
            published_iso = published_utc.isoformat()
        else:
            published_iso = None

        link = entry.get("link") or ""
        if not link:
            continue

        out.append(Item(
            title=_strip_html(entry.get("title") or "(no title)")[:300],
            url=link,
            source=name,
            source_category=category,
            published=published_iso,
            summary=_strip_html(entry.get("summary") or entry.get("description") or "")[:1200],
        ))
    return out


def fetch_tavily(query: str, api_key: str) -> list[Item]:
    try:
        from tavily import TavilyClient
    except ImportError:
        logging.warning("  ! tavily-python not installed; skipping discovery")
        return []
    try:
        client = TavilyClient(api_key=api_key)
        result = client.search(
            query=query,
            topic="news",
            days=2,
            max_results=5,
            search_depth="basic",
        )
    except Exception as exc:
        logging.warning("  ! discovery [%s]: %s", query, exc)
        return []
    out: list[Item] = []
    for r in result.get("results", []):
        url = r.get("url", "")
        if not url:
            continue
        out.append(Item(
            title=(r.get("title") or "(no title)")[:300],
            url=url,
            source=f"discovery: {query}",
            source_category="discovery",
            summary=(r.get("content") or "")[:1200],
        ))
    return out


# ---------------------------------------------------------------------------
# Synthesis
# ---------------------------------------------------------------------------

def synthesize(items: list[Item], api_key: str) -> dict:
    if not items:
        return {"summary": "Quiet day — no new items in the last 24h.", "sections": {}, "spiked": []}

    try:
        from anthropic import Anthropic
    except ImportError:
        logging.error("anthropic SDK not installed; falling back to raw links")
        return _raw_fallback(items, reason="anthropic SDK not installed")

    capped = items[:MAX_CANDIDATES_TO_SYNTHESIZE]
    payload = [
        {
            "i": idx,
            "title": item.title,
            "url": item.url,
            "source": item.source,
            "category": item.source_category,
            "summary": item.summary,
        }
        for idx, item in enumerate(capped)
    ]

    user_msg = (
        f"Today is {dt.date.today().isoformat()}. "
        f"Candidate items ({len(payload)} total):\n\n"
        f"{json.dumps(payload, ensure_ascii=False, indent=2)}"
    )

    try:
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model=SYNTHESIS_MODEL,
            max_tokens=8000,
            system=EDITORIAL_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}],
        )
    except Exception as exc:
        logging.error("synthesis call failed: %s", exc)
        return _raw_fallback(items, reason=f"synthesis failed: {exc}")

    text = "".join(block.text for block in response.content if getattr(block, "type", "") == "text")
    parsed = _extract_json(text)
    if not parsed:
        logging.error("synthesis returned unparseable JSON; falling back to raw")
        return _raw_fallback(items, reason="synthesis returned unparseable JSON")

    return _hydrate_briefing(parsed, capped, items)


def _extract_json(text: str) -> Optional[dict]:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start >= 0 and end > start:
            try:
                return json.loads(text[start : end + 1])
            except json.JSONDecodeError:
                return None
    return None


def _hydrate_briefing(parsed: dict, capped: list[Item], all_items: list[Item]) -> dict:
    sections: dict[str, list[dict]] = {}
    for section_name in SECTION_ORDER:
        raw = parsed.get("sections", {}).get(section_name, []) or []
        hydrated = []
        for entry in raw:
            idx = entry.get("i")
            if not isinstance(idx, int) or idx < 0 or idx >= len(capped):
                continue
            item = capped[idx]
            hydrated.append({
                "title": item.title,
                "url": item.url,
                "source": item.source,
                "take": (entry.get("take") or "").strip(),
                "plain_take": (entry.get("plain_take") or "").strip() if section_name == "Plumbing" else None,
            })
        if hydrated:
            sections[section_name] = hydrated

    spiked = []
    for entry in parsed.get("spiked", []) or []:
        idx = entry.get("i")
        if not isinstance(idx, int) or idx < 0 or idx >= len(capped):
            continue
        item = capped[idx]
        spiked.append({
            "title": item.title,
            "url": item.url,
            "source": item.source,
            "spiked_reason": (entry.get("spiked_reason") or "").strip() or "unspecified",
        })

    overflow = len(all_items) - len(capped)
    summary = (parsed.get("summary") or "").strip() or "Today's items below."
    if overflow > 0:
        summary += f" (+{overflow} items beyond synthesis cap — see spiked or next run.)"

    return {"summary": summary, "sections": sections, "spiked": spiked}


def _raw_fallback(items: list[Item], reason: str) -> dict:
    return {
        "summary": f"Synthesis unavailable — {reason}. Raw candidates below.",
        "sections": {
            "Raw items (synthesis unavailable)": [
                {
                    "title": item.title,
                    "url": item.url,
                    "source": item.source,
                    "take": (item.summary[:200] + "…") if len(item.summary) > 200 else item.summary,
                    "plain_take": None,
                }
                for item in items[:60]
            ]
        },
        "spiked": [],
    }


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_site(today_date: str, briefing: dict) -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    BRIEFINGS.mkdir(parents=True, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html", "htm", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    day_template = env.get_template("day.html.j2")
    (BRIEFINGS / f"{today_date}.html").write_text(
        day_template.render(date=today_date, briefing=briefing),
        encoding="utf-8",
    )

    archive: list[dict] = []
    for path in sorted(BRIEFINGS.glob("*.html"), reverse=True):
        stem = path.stem
        if stem == today_date:
            continue
        archive.append({"date": stem, "href": f"briefings/{path.name}"})

    index_template = env.get_template("index.html.j2")
    (DOCS / "index.html").write_text(
        index_template.render(today_date=today_date, briefing=briefing, archive=archive[:90]),
        encoding="utf-8",
    )

    style_src = TEMPLATES / "style.css"
    if style_src.exists():
        (DOCS / "style.css").write_text(style_src.read_text(encoding="utf-8"), encoding="utf-8")


def render_vault_markdown(today_date: str, briefing: dict) -> str:
    lines: list[str] = []
    lines.append("---")
    lines.append(f"date: {today_date}")
    lines.append("source: morning-brief")
    lines.append("type: briefing")
    lines.append("---")
    lines.append("")
    lines.append(f"# Morning Brief — {today_date}")
    lines.append("")
    if briefing.get("summary"):
        lines.append(f"> {briefing['summary']}")
        lines.append("")
    for section_name in SECTION_ORDER:
        items = briefing.get("sections", {}).get(section_name)
        if not items:
            continue
        lines.append(f"## {section_name}")
        lines.append("")
        for item in items:
            lines.append(f"- **[{item['title']}]({item['url']})** — *{item['source']}*")
            if item.get("take"):
                lines.append(f"  - {item['take']}")
            if item.get("plain_take"):
                lines.append(f"  - *Plain take:* {item['plain_take']}")
        lines.append("")
    if briefing.get("spiked"):
        lines.append("## Spiked")
        lines.append("")
        for s in briefing["spiked"]:
            lines.append(f"- [{s['title']}]({s['url']}) — {s['spiked_reason']}")
        lines.append("")
    return "\n".join(lines)


def write_vault(today_date: str, briefing: dict, vault_path: Path) -> Path:
    year = today_date.split("-")[0]
    target_dir = vault_path / "05 Reflections" / f"{year}-plan" / "briefings"
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{today_date}.md"
    target.write_text(render_vault_markdown(today_date, briefing), encoding="utf-8")
    return target


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Morning Brief: AI + Learning briefing scanner")
    ap.add_argument("--dry-run", action="store_true", help="Fetch + log only; write nothing")
    ap.add_argument("--write-vault", action="store_true", help="Also write markdown to Obsidian vault")
    ap.add_argument("--vault-path", type=str, default=os.environ.get("BRIEF_VAULT_PATH"),
                    help="Vault path (or set BRIEF_VAULT_PATH env var)")
    ap.add_argument("--lookback-hours", type=int, default=24, help="How far back to look (default 24)")
    ap.add_argument("--no-discovery", action="store_true", help="Skip Tavily discovery even if key is set")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(message)s")

    sources = yaml.safe_load(SOURCES_PATH.read_text(encoding="utf-8"))

    lookback = args.lookback_hours
    if dt.datetime.now().weekday() == 0:  # Monday: catch the weekend
        lookback = max(lookback, 60)
    since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=lookback)
    logging.info("Looking back %sh (since %s UTC)", lookback, since.isoformat(timespec="minutes"))

    seen = load_seen()
    all_items: list[Item] = []

    logging.info("Fetching %d RSS feeds…", len(sources.get("feeds", [])))
    for source in sources.get("feeds", []):
        items = fetch_rss(source, since)
        new = [x for x in items if url_key(x.url) not in seen]
        logging.info("  %s — %d fetched, %d new", source["name"], len(items), len(new))
        all_items.extend(new)

    tavily_key = os.environ.get("TAVILY_API_KEY")
    if tavily_key and not args.no_discovery:
        queries = sources.get("discovery_queries", [])
        logging.info("Running %d discovery queries…", len(queries))
        for query in queries:
            items = fetch_tavily(query, tavily_key)
            new = [x for x in items if url_key(x.url) not in seen]
            logging.info("  discovery[%s] — %d fetched, %d new", query, len(items), len(new))
            all_items.extend(new)
    else:
        if not tavily_key:
            logging.info("TAVILY_API_KEY not set — skipping discovery searches")
        else:
            logging.info("--no-discovery — skipping discovery searches")

    seen_urls: set[str] = set()
    deduped: list[Item] = []
    for item in all_items:
        if item.url in seen_urls:
            continue
        seen_urls.add(item.url)
        deduped.append(item)
    all_items = deduped
    logging.info("Total candidate items (deduped): %d", len(all_items))

    if args.dry_run:
        logging.info("Dry run — no files written")
        return 0

    today_date = dt.date.today().isoformat()
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    if not anthropic_key:
        logging.warning("ANTHROPIC_API_KEY not set — publishing raw fallback")
        briefing = _raw_fallback(all_items, reason="ANTHROPIC_API_KEY not configured")
    else:
        briefing = synthesize(all_items, anthropic_key)

    render_site(today_date, briefing)
    logging.info("Wrote docs/briefings/%s.html and refreshed docs/index.html", today_date)

    if args.write_vault:
        if not args.vault_path:
            logging.error("--write-vault requires --vault-path or BRIEF_VAULT_PATH env var")
            return 2
        vault_path = Path(args.vault_path).expanduser()
        if not vault_path.exists():
            logging.error("vault path does not exist: %s", vault_path)
            return 2
        written = write_vault(today_date, briefing, vault_path)
        logging.info("Wrote vault copy: %s", written)

    now_ts = int(dt.datetime.now(dt.timezone.utc).timestamp())
    for item in all_items:
        seen[url_key(item.url)] = now_ts
    save_seen(seen)

    section_counts = {name: len(items) for name, items in briefing.get("sections", {}).items()}
    logging.info("Sections: %s | spiked: %d",
                 ", ".join(f"{k}={v}" for k, v in section_counts.items()) or "(none)",
                 len(briefing.get("spiked", [])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
