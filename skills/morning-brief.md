---
name: morning-brief
description: Generate today's AI + Learning briefing on demand. Pulls RSS + discovery searches, synthesizes via Claude, writes the website and a copy into the Obsidian vault. Run when you want the briefing now rather than waiting for the cron, or when you specifically want a vault copy for the day's planning context.
---

# /morning-brief

Generates today's AI + Learning industry briefing using the scanner at `briefing/scan.py`. Same code path the GitHub Actions cron uses — running this locally just adds the vault write.

## When to run
- You want today's briefing immediately rather than waiting for the next 11:00 UTC cron tick
- You want today's briefing in your Obsidian vault (cron-driven runs in CI cannot reach your local vault)
- You changed `briefing/sources.yml` or the editorial prompt and want to regenerate

## Setup (one-time)

Environment variables — set in your shell profile or pass inline:

| Variable | Purpose |
|---|---|
| `ANTHROPIC_API_KEY` | Required for synthesis. If unset, briefing falls back to raw links. |
| `TAVILY_API_KEY` | Optional. If unset, discovery searches are skipped and the scanner uses curated RSS only. |
| `BRIEF_VAULT_PATH` | Path to your Obsidian vault root. Required for the vault write step. |

Install dependencies once:

```bash
cd briefing
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Steps for Claude when invoked

1. Confirm required env vars are set:
   ```bash
   echo "ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:+set}"
   echo "BRIEF_VAULT_PATH: $BRIEF_VAULT_PATH"
   ```
   If `BRIEF_VAULT_PATH` is empty, ask the user for the vault path before proceeding.

2. Run the scanner with vault write:
   ```bash
   python briefing/scan.py --write-vault --vault-path "$BRIEF_VAULT_PATH"
   ```

3. If the run succeeded, commit and push:
   ```bash
   git add docs/ briefing/seen.json
   git diff --quiet --staged || git commit -m "morning brief $(date -u +%Y-%m-%d)"
   git push
   ```

4. Report back to the user:
   - Today's date
   - Counts per section (the scanner logs these)
   - Path to the vault file just written
   - Link to the live site

## What got built / where

- `briefing/scan.py` — the scanner
- `briefing/sources.yml` — RSS feed list + discovery queries. Edit this to tune what's pulled.
- `briefing/templates/` — Jinja2 templates + CSS for the website
- `briefing/seen.json` — dedupe state; committed back each run
- `docs/` — generated site (GitHub Pages serves from here)
- `.github/workflows/morning-brief.yml` — daily cron at 11:00 UTC

## Tuning the editorial voice

The synthesis prompt lives in `briefing/scan.py` as `EDITORIAL_SYSTEM_PROMPT`. It encodes:
- Promote/demote rules (AI-native vs. vendor PR, mechanism vs. listicles)
- The reader's actual toolset (Pi, Codex, Claude Code, Claude Desktop — NOT Cursor/Copilot/Windsurf)
- The "Plain take" rule for Plumbing items (non-engineer explainers)
- The 7-section taxonomy

When the briefing surfaces too much vendor noise or skips too much craft, edit that prompt. The spiked-list at the bottom of each day's page shows what got filtered and why — use it to tune.

## Source-list balance rule

`briefing/sources.yml` aims for gender balance and worldview diversity (builders + critics + practitioners + researchers). When you edit it, hold the balance. Adding 5 male VC voices and dropping a critic is a regression.
