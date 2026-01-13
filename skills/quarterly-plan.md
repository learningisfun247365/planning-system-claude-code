# Quarterly Planning Skill

## Purpose

The quarterly sit-down that reviews the past 12 weeks, surfaces patterns from monthly syntheses, and sets 2-3 focus areas for the next quarter. This is a 3-hour session that includes deep reflection, manual review of analog sources, and intentional planning.

**Core insight:** The quarterly is where pattern recognition happens at scale. Monthly syntheses roll up, tracker data reveals trends, and you step back to see the bigger picture before diving into the next 12 weeks.

---

## When to Use

- **Timing:** Week 11 of current quarter (one week before quarter ends - gives time to act on insights)
- User says "plan Q1", "quarterly planning", "12-week plan"
- Beginning of year planning (includes annual review connection)

---

## Files This Skill Reads

**For Context:**
1. **Annual plan:** `[vault]/[reflections]/[year]-plan/[year]-plan.md`
   - Values, identity focus, annual milestones, your rules

**For Review:**
2. **Current quarter plan:** `[vault]/[reflections]/[year]-plan/Q[X]-[year]-plan.md`
   - What was planned, lead/lag measures to review, weekly schedules
3. **Monthly plan files:** `[vault]/[reflections]/[year]-plan/[month]-[year].md` (3 files)
   - Monthly syntheses, patterns, what got attention/neglected
4. **Weekly reflection files:** `[vault]/[reflections]/[MM.DD.YY]-[MM.DD.YY].md` (12-13 files)
   - Raw weekly reflections for the quarter - themes, energy patterns, what got attention/neglected at the granular level
5. **Daily tracker CSV:** User provides (downloaded from Google Sheets or other tracker)
   - Daily reflections, health metrics, mood, sleep patterns across quarter

**For Planning:**
6. **Active projects:** `[vault]/[projects]/Active-Projects.md`
7. **Editorial calendar:** `[vault]/[writing]/editorial-calendar.md`
8. **Cultural activities ideas:** `[vault]/[reflections]/[year]-plan/cultural-activities-ideas.md`
   - Master list of cultural activities to consider for QoL minimums

---

## Files This Skill Writes

- `[vault]/[reflections]/[year]-plan/Q[X]-[year]-plan.md`

---

## The Process (3 hours total)

### Phase 1: Gather + Review (90 min)

This phase is about looking back before looking forward. Don't rush it. Ask questions to ensure you're looking across all fields of life.

#### Step 1: Read the Annual Plan

Read `[year]-plan.md` and surface:
- Your values and their gaps
- Identity focus
- Key milestones
- Your rules (external structure, transition protocol, etc.)

Output:
> "Here's what you set for [YEAR]:
>
> **Values:** [Your values]
> **Identity focus:** [What you're becoming]
> **Milestones:** [Key targets]
>
> Let's see how Q[X] aligned with this."

#### Step 2: Review Current Quarter's Plan

Read current quarter's plan and create a review prompt:

> **Lag Measures Check:**
> - [Lag measure 1]: Target was [X]. Did you hit it?
> - [Lag measure 2]: Target was [X]. Did you hit it?
> - [Lag measure 3]: Target was [X]. Did you hit it?
>
> **Lead Measures Check:**
> - [Lead measure 1]: Target was [X]% [frequency]. What actually happened?
> - [Lead measure 2]: Target was [X]% [frequency]. What actually happened?
>
> Don't answer yet - we'll gather more data first.

#### Step 3: Review Monthly Syntheses

Read the 3 monthly plan files from this quarter. For each month, extract:
- Recurring themes
- Energy patterns
- What got attention vs. neglected
- Open threads carried forward

Output:
> **Monthly Patterns Across Q[X]:**
>
> **[Month 1]:**
> - Themes: [X]
> - Energy: [high/low pattern]
> - Attention: [what got focus]
> - Neglected: [what didn't]
>
> **[Month 2]:**
> - Themes: [X]
> - Energy: [high/low pattern]
> - Attention: [what got focus]
> - Neglected: [what didn't]
>
> **[Month 3]:**
> - Themes: [X]
> - Energy: [high/low pattern]
> - Attention: [what got focus]
> - Neglected: [what didn't]
>
> **Cross-month patterns:**
> - What themes appeared in 2+ months?
> - What kept getting neglected?
> - What energy patterns repeat?

#### Step 4: Review Daily Tracker Data

Ask user to provide the CSV:
> "Paste or attach your daily tracker CSV for Q[X] (all 12 weeks). I'll analyze patterns across the quarter."

Once provided, analyze for:

**Patterns to Surface (show, don't interpret):**
- Exercise: Days/week average, trend over quarter, any gaps
- Alcohol: % of days, trend (stable/climbing/declining), any spikes
- Food quality: Distribution, any sustained patterns
- Mood: Patterns, any correlations visible
- Sleep: Average, any sustained poor periods
- Weight: Trend over quarter

Output:
> **Tracker Patterns (Q[X] - 12 weeks):**
>
> | Metric | Average | Trend | Notable |
> |--------|---------|-------|---------|
> | Exercise | [X] days/week | [stable/up/down] | [gaps or spikes] |
> | Alcohol | [X]% of days | [stable/climbing/declining] | [any spikes] |
> | Food | [pattern] | [pattern] | [sustained periods] |
> | Mood | [pattern] | [any correlations] | |
> | Sleep | [X] hrs avg | [pattern] | [poor periods] |
> | Weight | [trend] | | |
>
> **What correlations do you see?** (e.g., alcohol climbs when exercise drops, mood dips correlate with sleep, etc.)

#### Step 5: Manual Review Prompts

**This is critical.** The skill can't read analog sources - prompt user to review them:

> **Analog Review (take 20-30 minutes):**
>
> Before we continue, go through these sources manually:
>
> **1. Journal entries from Q[X]:**
> - Flip through your journal from the past 12 weeks
> - What emotions come up repeatedly?
> - What were you wrestling with?
> - Any breakthroughs or insights you wrote down?
>
> **2. Photos from Q[X]:**
> - Scroll through your camera roll for the past 3 months
> - What did you actually DO? (vs. what you planned)
> - What moments did you capture?
> - What's missing that you wish you'd done?
>
> **3. Calendar review:**
> - Look at your actual calendar for the past 12 weeks
> - How many date nights actually happened?
> - How many cultural activities?
> - How many friend gatherings?
> - What got cancelled or skipped?
>
> **4. Physical planner observations:**
> - Flip through your weekly spreads
> - What notes did you write to yourself?
> - What patterns do you see in your handwriting/energy?
> - Any weeks that stand out as particularly good or bad?
>
> Come back when you've reviewed these. We'll reflect together.

**STOP HERE.** Wait for user to complete manual review before Phase 2.

---

### Phase 2: Reflection (30 min)

#### Step 6: Synthesis Prompts

After user has reviewed analog sources, prompt reflection:

> **Quarter Reflection Questions:**
>
> Based on everything you've reviewed - tracker data, monthly syntheses, journal, photos, calendar, planner:
>
> 1. **Lag measures:** Which hit? Which missed? Why?
>
> 2. **Lead measures:** Did you maintain the behaviors? What got in the way?
>
> 3. **Identity evidence:**
>    - Did you push through when things got hard/boring?
>    - Did you keep rhythms during disruptions?
>    - What community actually happened?
>
> 4. **The honest answer:** What's the real story of this quarter? (Not the planned story - the actual one)
>
> 5. **Structure check:** What external commitments ended? Did you replace them in time?
>
> 6. **What worked** that you want to keep?
>
> 7. **What didn't work** that you want to change?
>
> 8. **What surprised you** when you reviewed the photos and journal?
>
> Take 15-20 minutes to think through these. Write notes if helpful. When you're ready, we'll plan Q[next].

**PAUSE.** Wait for user to reflect before Phase 3.

---

### Phase 3: Planning (60 min)

#### Step 7: Apply Periodization

Based on which quarter, set the frame:

**Q1-Q2 (Build Phases):**
> "This is a build quarter. The question is: What ONE new structure do you want to start? New class, new commitment, new recurring activity. Pick one that adds external accountability."

**Q3 (Maintenance Phase):**
> "This is maintenance season. Summer disrupts routines. The question is: What's the minimum to maintain through summer? Don't add new things. Protect what exists."

**Q4 (Protection Phase):**
> "This is protection season. November-December collapse is the pattern. The question is: What anchor prevents the collapse? What one commitment will you NOT drop even when everything feels hard?"

#### Step 8: Identify Focus Areas (2-3 max)

Guide user to pick 2-3 focus areas from their life domains:
- Relationship
- Self
- Community
- Career

**Constraint:** Maximum 3 focus areas. If they want more, force prioritization:

> "You have 3 focus areas. Adding a 4th means one of these won't get real attention. Which one are you willing to drop? Or is this new thing actually more important than something already listed?"

For each focus area, prompt:

> **[Focus Area Name]**
> - What domain does this serve?
> - Why does this matter this quarter specifically?
> - What does success look like at end of quarter? (Lag measure - make it observable)
> - What 2-3 weekly/daily behaviors drive that outcome? (Lead measures)
> - What % target for each lead measure? (85% is the standard)

#### Step 9: Map Calendar Constraints

Ask:
- "What travel is planned this quarter?"
- "What major events or commitments are already locked?"
- "What weeks are unusable for focused work?"

Create a 12-week calendar overview showing constraints.

#### Step 10: Flag Structure Transitions

**This is critical.** Look for:
- Any 12-week class/commitment ending mid-quarter
- Any recurring structure that's about to stop
- Any gap between "current structure ends" and "next structure begins"

If a structure ends in weeks 1-8, be insistent:

> "I see [class/commitment] ends in week [X]. What's replacing it? This is the pattern that leads to deterioration. We need a plan now, not when it ends. What are your options? When will you sign up?"

#### Step 11: Set Quality of Life Minimums

First, check `cultural-activities-ideas.md`:

> "Here's what's in your cultural activities ideas list. Anything here that should anchor the quarter? Any big events or limited-run shows you'd regret missing?"

Based on quarterly focus and constraints, set minimums:

> **Quality of Life Minimums for Q[X]:**
>
> | Domain | Minimum | Notes |
> |--------|---------|-------|
> | Date nights | [frequency] | |
> | Cultural activity | [frequency] | |
> | Body ritual | [frequency] | |
> | Community | [frequency] | |
> | Exercise | [frequency] | Protect this - it's working |

#### Step 12: Generate the Plan Document

Create `[reflections]/[year]-plan/Q[X]-[year]-plan.md`:

```markdown
# Q[X] [YEAR] Plan

**Created:** [Date]
**Weeks:** [Week range] ([Date range])
**Theme:** [Short theme if applicable]
**Periodization:** [Build/Maintenance/Protection]

---

## Review of Q[Previous]

**Lag measures:**
- [Measure 1]: [Hit/Missed] - [brief note]
- [Measure 2]: [Hit/Missed] - [brief note]
- [Measure 3]: [Hit/Missed] - [brief note]

**What worked:** [Keep this]

**What didn't work:** [Change this]

**Key insight:** [One sentence from reflection]

**Tracker trends:** [Brief summary of quarter patterns]

---

## Identity Focus

**Becoming someone who:**
- [Identity trait 1]
- [Identity trait 2]
- [Identity trait 3]

**Evidence from Q[Previous]:**
- [What happened]
- [What happened]
- [What happened]

---

## Q[X] Focus Areas

### 1. [Focus Area Name]
**Domain:** [Relationship / Self / Community / Career]
**Why this quarter:** [One sentence]

**Lag Measure:** [Observable outcome by end of quarter]

**Lead Measures:**
| Behavior | Frequency | Target |
|----------|-----------|--------|
| [Behavior 1] | [X/week] | [85%] |
| [Behavior 2] | [X/week] | [85%] |

**Structure:** [When/how this happens in the week]

---

### 2. [Focus Area Name]
**Domain:** [Domain]
**Why this quarter:** [Why]

**Lag Measure:** [Observable outcome]

**Lead Measures:**
| Behavior | Frequency | Target |
|----------|-----------|--------|
| [Behavior 1] | [X/week] | [85%] |
| [Behavior 2] | [X/week] | [85%] |

**Structure:** [When/how]

---

### 3. [Focus Area Name] (if applicable)
[Same structure]

---

## Calendar Constraints

| Week | Dates | Constraint | Impact |
|------|-------|------------|--------|
| [X] | [Dates] | [What's happening] | [How it affects focus] |

---

## Structure Transition Alerts

| Current Structure | Ends | Replacement | Status |
|-------------------|------|-------------|--------|
| [Name] | Week [X] | [Plan] | [Signed up / Need to find / At risk] |

**Week 8 action:** [What to research/sign up for by week 8]

---

## Quality of Life Minimums

| Domain | Minimum | Notes |
|--------|---------|-------|
| Date nights | [Frequency] | |
| Cultural activity | [Frequency] | |
| Body ritual | [Frequency] | |
| Community | [Frequency] | |
| Exercise | [Frequency] | Protect this |

---

## Weekly Check-in Questions

During Sunday planning, ask:
1. Did I hit 85% on lead measures?
2. What's my one thing that can't slip this week?
3. Is there a date night scheduled?
4. Am I at 70% capacity or overloaded?

---

## Week 11: Q[X] Review Prompts

**Lag measures:**
- [Measure 1]: Hit / Missed
- [Measure 2]: Hit / Missed

**Identity evidence:**
- [Evidence question specific to this quarter's focus]
- [Evidence question]
- [Evidence question]

**Manual review reminder:**
- Journal entries
- Photos from quarter
- Calendar actuals vs. planned
- Planner observations

**Tracker patterns to review:**
- Exercise trend
- Alcohol trend
- Mood patterns
- Correlations
```

---

## Boundaries

### This Skill Does:
- Read annual plan and surface relevant context
- Read monthly syntheses and individual weekly reflections
- Analyze daily tracker CSV for quarter-level patterns
- Prompt manual review of analog sources (journal, photos, calendar, planner)
- Guide through focus area selection with prompts
- Map calendar constraints
- Flag structure transitions aggressively
- Generate the quarterly plan document

### This Skill Does NOT:
- Fill in the thinking for you (prompts, not answers)
- Read your journal, photos, or planner (you do that manually)
- Interpret what tracker patterns mean (that's your reflection)
- Add more than 3 focus areas (enforce the limit)
- Ignore structure transition risks
- Create detailed weekly or monthly plans (those are other skills)
- Rush the review phase (this is a 3-hour sit-down)

---

## Voice

Be direct. Challenge scope creep. On structure transitions, be insistent - this is where the system has historically failed.

Don't be deferential. If something doesn't make sense, say so. If a focus area is vague, push for specificity. If a lead measure isn't actually measurable, call it out.

On the manual review:
> "I can read the digital files, but the real insights are in your analog sources. Take the time to flip through your journal, scroll through photos, look at what actually happened on your calendar. That's where the truth lives."

On pacing:
> "This is 3 hours for a reason. Don't rush the review to get to planning. The review IS the work - planning is just capturing decisions."

---

## Chains To

After completing quarterly planning:

> "Quarterly plan is set. Next step: Run `/monthly-plan` to plan the first month of Q[X]. This includes monthly synthesis, content planning, QoL booking, and [partner] email."

---

## Example Invocation

```
/quarterly-plan
```

Or: "Let's plan Q2"

Or: "Time for quarterly planning - here's my tracker CSV [paste]"

Or: "It's week 11, time to review the quarter"
