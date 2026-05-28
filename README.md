# Planning System for Claude Code

A cascading planning system using Claude Code skills. Annual direction flows to quarterly focus, then monthly booking, then weekly intentions.

**Read the full piece:** [How I Used Claude Code to Build My Planning System (So I Could Stop Planning)](https://substack.com/home/post/p-184651031)
---

## What This Is

Five Claude Code skills that guide you through planning and note processing:

### Planning Skills

| Skill | Timing | Duration | Purpose |
|-------|--------|----------|---------|
| `/quarterly-plan` | Week 11 of each quarter | 3 hours | Review 12 weeks, set 2-3 focus areas, flag structure transitions |
| `/monthly-plan` | 3rd/4th Sunday of month | 2 hours | Synthesize month, plan content, book QoL activities |
| `/weekly-plan` | Every Sunday | 30-45 min | Surface patterns, plan next week, create reflection file |

**The cascade:** Quarterly sets the focus areas. Monthly books the life stuff. Weekly checks the pulse and creates next week's file with priorities loaded.

### Processing Skills (NEW)

| Skill | Timing | Purpose |
|-------|--------|---------|
| `/journal-process` | After voice recording | Clean up voice transcripts, infer structure, append to weekly reflection |
| `/daily-process` | End of day / weekly | Scan vault for unfiled notes, add metadata, move to correct folders |

**The lesson:** These skills are only useful if they're chained to something you already do. `/daily-process` was built and forgotten for months because it had no trigger. Now it chains from `/weekly-plan` and `/journal-process`.

### Intel Skill (NEW)

| Skill | Timing | Purpose |
|-------|--------|---------|
| `/morning-brief` | Daily (auto via cron, manual on demand) | Scan AI + Learning industry sources, synthesize today's signal, publish to website + vault |

The first **outward-facing** piece of this system. See [the Daily Briefing section below](#daily-briefing-morning-brief) for setup.

---

## Prerequisites

These skills assume you have:

1. **A notes system** (Obsidian, Notion, etc.) with:
   - Daily/weekly reflection files
   - A place for plans (quarterly, monthly)
   - An ideas inbox for writing
   - An editorial calendar (if you publish)

2. **A daily tracker** (optional but useful for quarterly review). 
   - Can be Google Sheets, a habit tracker, or paper
   - Tracks: exercise, sleep, mood, etc.

3. **Claude Code** installed and configured

---

## Setup

> **Tip:** If you're using Claude Code (in VS Code, Cursor, or terminal), you can ask it to help you set up. Say something like "Help me configure these planning skills for my notes system" and it will search your file structure, find your existing folders, and update the placeholders with your actual paths.

### 1. Update the file paths

Each skill has placeholder paths like `[vault]/[reflections]/`. Replace these with your actual paths:

| Placeholder | Example |
|-------------|---------|
| `[vault]` | `obsidian-vault` or `notes` |
| `[reflections]` | `05 Reflections` or `journal` |
| `[writing]` | `07 Writing` or `content` |
| `[templates]` | `00 Meta/Templates` or `templates` |
| `[projects]` | `06 Projects` or `projects` |
| `[year]-plan` | `2025 plan` or `2025` |

### 2. Create the required files

**Minimum files needed:**

```
[vault]/
├── [reflections]/
│   ├── [year]-plan/
│   │   ├── [year]-plan.md           # Annual plan (values, milestones)
│   │   ├── Q1-[year]-plan.md        # Quarterly plans (skill generates these)
│   │   ├── january-[year].md        # Monthly plans (skill generates these)
│   │   └── cultural-activities-ideas.md
│   └── [MM.DD.YY]-[MM.DD.YY].md     # Weekly reflection files (skill generates these)
├── [templates]/
│   └── weekly-reflection.md         # Template for weekly files - skill uses this
└── [writing]/                        # Optional - for content planning
    ├── editorial-calendar.md
    ├── ideas/inbox.md
    └── drafts/
```

> **Note:** The skills contain embedded output templates. When you run `/quarterly-plan`, `/monthly-plan`, or `/weekly-plan`, Claude generates the plan files using the format defined in each skill. You don't need separate template files for plans - the skills handle that.

### 3. Install the skills

Copy the skill files to your Claude Code skills directory:

```bash
# Copy to your .claude/skills folder
cp skills/quarterly-plan.md ~/.claude/skills/quarterly-plan.md
cp skills/monthly-plan.md ~/.claude/skills/monthly-plan.md
cp skills/weekly-plan.md ~/.claude/skills/weekly-plan.md
cp skills/journal-process.md ~/.claude/skills/journal-process.md
cp skills/daily-process.md ~/.claude/skills/daily-process.md
```

Or create a project-level `.claude/skills/` folder in your notes directory.

---

## Usage

### Quarterly Planning (Week 11)

```
/quarterly-plan
```

What it does:
- Reads annual plan, current quarter plan, monthly files, weekly reflections
- Analyzes daily tracker data (you provide CSV)
- Prompts manual review of journal, photos, calendar
- Guides you to 2-3 focus areas with lead/lag measures
- Flags structure transitions (classes ending, etc.)
- Creates next quarter's plan file

### Monthly Planning (3rd/4th Sunday)

```
/monthly-plan
```

What it does:
- Synthesizes weekly reflections from the month
- Reviews editorial calendar and ideas inbox
- Walks through QoL booking: date nights, cultural activities, body rituals, community
- Drafts partner email with date night options
- Creates month plan file

### Weekly Planning (Every Sunday)

```
/weekly-plan
```

What it does:
- Surfaces patterns from past week's reflection
- Pulls context from monthly/quarterly plans
- Reality-checks capacity
- Creates next week's reflection file with priorities at top
- Flags warning signs (overcommitment, social gaps)

---

## Customization

### Remove sections you don't need

- **No partner?** Remove the [partner] email section from monthly-plan
- **Don't write content?** Remove editorial calendar references
- **No daily tracker?** Skip Step 4 in quarterly-plan

### Adjust the domains

The skills reference these life domains:
- Relationship
- Self
- Community
- Career

Change these to match how you think about your life.

### Change the cadence

- Weekly planning assumes Sunday. Change "Sunday" references if you plan on a different day
- Monthly planning assumes 3rd/4th Sunday. Adjust timing notes as needed

---

## The Philosophy

**Why this exists:** With ADHD (or just a busy life), the gap between "I know what I should do" and "I actually do it" is massive. Implementation intentions - specific plans for when/where/how - close that gap.

**What AI does:** Surfaces patterns, reminds you what you committed to, flags when you're overcommitting or neglecting something. It holds the context you can't.

**What you do:** Make meaning from the patterns, make decisions, do the actual work.

The system doesn't make you more disciplined. It makes discipline irrelevant by externalizing the prompts and triggers.

---

## Daily Briefing (morning-brief)

A daily AI + Learning industry scanner. Pulls RSS + discovery searches every morning, asks Claude to filter and route into themed sections, publishes the result as a static site (GitHub Pages) and writes a markdown copy into your vault when run locally.

### What it covers

Seven editorial sections, calibrated for a constructivist-humanist instructional designer who's technical-non-technical:

1. **Plumbing** — memory, agents, context engineering, MCP, evals (each item gets a plain-language "Plain take" line)
2. **New Modes of Doing** — AI-native ways of getting employees what they need to know when they need it
3. **ID Craft** — instructional design as a craft (design thinking, action mapping, evidence-based)
4. **Org & Talent Design** — how AI-native orgs are restructuring roles and skill ladders
5. **Steering & Judgment** — critical thinking, evals, parallel-track work, epistemic skepticism
6. **Cross-Pollination** — borrowings from cog sci, design, neuroscience, complexity, applied to learning
7. **Cool & Weird** — outliers and building-in-public

Each surviving item gets a one-sentence *take* (not a summary). Spiked items show at the bottom with a reason.

### How it runs

**Automated:** `.github/workflows/morning-brief.yml` runs daily at 11:00 UTC, commits the generated `docs/` files, GitHub Pages auto-publishes.

**Manual:** `/morning-brief` slash command does the same, plus writes a markdown copy to your vault at `[vault]/05 Reflections/[year]-plan/briefings/YYYY-MM-DD.md`.

### Setup

1. **Install Pages**: Repo Settings → Pages → Source: deploy from a branch → `main` / `/docs` folder.
2. **Add secrets**: Repo Settings → Secrets and variables → Actions:
   - `ANTHROPIC_API_KEY` (required for synthesis)
   - `TAVILY_API_KEY` (optional; enables discovery searches beyond RSS)
3. **Trigger first run**: Actions tab → "Morning Brief" → "Run workflow", or wait for the next 11:00 UTC tick.
4. **For local manual runs**: set `BRIEF_VAULT_PATH` in your shell, then `/morning-brief`.

### Tuning

- **Sources**: edit `briefing/sources.yml`. Source list balance is intentional — gender + worldview diversity. Hold it when editing.
- **Editorial voice**: edit `EDITORIAL_SYSTEM_PROMPT` in `briefing/scan.py`. The spiked-list at the bottom of each daily page shows what got filtered and why — use it to tune.
- **Cron timing**: edit the `cron:` line in `.github/workflows/morning-brief.yml`.

### Files

```
briefing/
├── scan.py              # the scanner
├── sources.yml          # RSS feeds + discovery queries
├── templates/           # Jinja2 templates + CSS
└── seen.json            # dedupe state (committed each run)
docs/                    # generated site (Pages serves this)
.github/workflows/
└── morning-brief.yml    # daily cron
skills/
└── morning-brief.md     # slash command for manual runs
```

---

## License

MIT - use however you want.

---

## Questions?

[Substack article placeholder] - explains the thinking behind this system.
