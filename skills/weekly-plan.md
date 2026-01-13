# Weekly Planning Skill

## Purpose

The Sunday session that reviews the past week and plans the next. AI does the pattern surfacing (what happened, what patterns emerged) so you can make decisions and move forward without getting stuck in reflection.

**Core insight:** With ADHD, external memory and context windows are challenging. AI surfaces patterns and reminds you what you're working towards. You make meaning and decide what's next.

**Duration:** 30-45 minutes

---

## When to Use

- **Timing:** Every Sunday
- User says "weekly planning", "plan my week", "weekly review"
- After monthly planning (to maintain weekly rhythm through the month)

---

## Files This Skill Reads

**For Synthesis:**
1. **Current week's reflection:** `[vault]/[reflections]/[MM.DD.YY]-[MM.DD.YY].md`

**For Planning:**
2. **Monthly plan:** `[vault]/[reflections]/[year]-plan/[month]-[year].md` (for focus areas, content/QoL commitments)
3. **Quarterly plan:** `[vault]/[reflections]/[year]-plan/Q[X]-[year]-plan.md` (for strategic context)
4. **Cultural activities ideas:** `[vault]/[reflections]/[year]-plan/cultural-activities-ideas.md`
   - Check if anything interesting is coming up this week

**For File Creation:**
5. **Weekly reflection template:** `[vault]/[templates]/weekly-reflection.md`

---

## Files This Skill Writes/Updates

- Updates the **Sunday Synthesis** section in current week's reflection file
- Creates **next week's reflection file:** `[vault]/[reflections]/[MM.DD.YY]-[MM.DD.YY].md`
  - Includes Week Priorities section at top with this week's focus and commitments

---

## The Process (30-45 min)

### Phase 1: Weekly Synthesis (15 min)

#### Step 1: Locate Reflection File

Ask:
> "Which week are we reviewing and planning? (Provide start date, e.g., 12.22.24)"

Use Glob to find the file: `**/[reflections]/[MM.DD.YY]-[MM.DD.YY].md`

If multiple matches or no match, show available files and ask user to specify.

#### Step 2: Surface Patterns (AI Does This Work)

Read the reflection file and analyze:

**Recurring themes:**
- Topics/ideas mentioned 2+ times across days
- Questions that came up repeatedly
- `[[Wikilinks]]` referenced multiple times

**Energy patterns:**
- Which days felt energized vs depleted?
- What activities got attention?
- What got dropped or neglected?

**Reading/media consumed:**
- Books, articles, podcasts - any thematic coherence?

**Unfinished threads:**
- Questions raised but not answered
- Ideas mentioned but not developed

**Output:**
> **Week Synthesis: [Date Range]**
>
> **Recurring themes this week:**
> - [Theme 1]: Appeared [X] times (context: [brief note])
> - [Theme 2]: Appeared [X] times
>
> **Energy patterns:**
> - High energy: [which days, what was happening]
> - Low energy: [which days, what was different]
>
> **What got attention:**
> - [Domain/project/activity that got energy]
>
> **What got neglected:**
> - [Domain/project that didn't get attention]
>
> **Wikilinks (potential ideas to develop):**
> - [[link1]] - appeared [X] times
> - [[link2]]
>
> **Reading this week:**
> - [Title/source]: [brief note on relevance]
>
> **Open threads:**
> - [Question or idea needing attention]

#### Step 3: Quick Reflection Prompt

Prompt user (don't answer for them):

> **Quick reflection questions:**
> 1. What's one pattern that stands out?
> 2. Any open thread ready to become something (article, project, conversation)?
> 3. What energy pattern do you notice, and what does it tell you?
>
> Take 2-3 minutes, then let's plan next week.

**BRIEF PAUSE.** Wait for quick input, then move to planning.

---

### Phase 2: Planning Next Week (15-20 min)

#### Step 4: Pull Context

**Read monthly plan** for this week's focus:
- Focus areas for the month
- Content calendar (any articles due next week?)
- QoL bookings (date nights, cultural activities, body rituals scheduled?)

**Read quarterly plan** for broader strategic context if needed.

**Output:**
> **Context for Next Week:**
>
> **This month's focus areas:**
> - [Focus area 1]
> - [Focus area 2]
>
> **Content:** [Article due dates if any]
>
> **QoL scheduled:** [Date night, cultural activity, body ritual?]

#### Step 5: Capacity Reality Check

Ask:
> "What's your week look like?
> - Work meetings/commitments?
> - Energy level forecast? (realistic, not aspirational)
> - Available hours for project work? (be honest)"

**Flag capacity issues:**
- If user lists 20 hours of projects but only has 5 hours available: "That's 4x over capacity. What's the ONE thing that matters most?"
- If commitments leave no buffer: "This assumes perfect conditions. What's the realistic version?"

#### Step 6: Plan Next Week

For each domain, determine concrete next actions:

**Strategic projects** (if applicable):
- What moves each active project forward?
- Specific tasks (2-3 max per project)
- Time needed

**Content/writing:**
- Any article due this week?
- Drafting, editing, or research time needed?

**QoL commitments:**
- Anything scheduled that needs prep?
- Any gaps that need filling (2+ weeks without social plans)?
- Check `cultural-activities-ideas.md` - anything interesting happening this week?

**Output:**
> **Next Week Plan: [Date Range]**
>
> **Strategic Projects:**
> - **[Project 1]:** [This week's focus]
>   - [ ] [Concrete task 1]
>   - [ ] [Concrete task 2]
>   - Time: [X hours]
>
> **Content:**
> - [ ] [Article due / Draft to finish / Research topic]
> - Time: [X hours]
>
> **QoL:**
> - [Date night / Cultural activity / Body ritual scheduled]
> - [ ] Prep needed: [if applicable]
>
> **Community:**
> - [Friend/social plan, or flag gap if none]
>
> **Total project time:** [X hours] | **Available:** [Y hours]

#### Step 7: Reality Check & Adjust

**If over capacity:**
> "You have [X] hours of work planned and [Y] hours available. What drops or gets less time?"

**If significant gaps:**
> "No social plans for 2 weeks. This is a warning sign. Can we add one small thing?"

**If blockers exist:**
> "Project X is blocked by Y. What needs to happen to unblock it?"

---

### Phase 3: Finalize (5-10 min)

#### Step 8: Update Sunday Synthesis Section

Update the current week's reflection file with the synthesis output.

**CRITICAL:** Use Edit tool to replace ONLY the Sunday Synthesis section. NEVER delete Monday-Saturday daily entries.

#### Step 9: Create Next Week's Reflection File

Calculate next week's date range (Monday to Sunday).

**Use template:** `[vault]/[templates]/weekly-reflection.md`

Create file at `[vault]/[reflections]/[MM.DD.YY]-[MM.DD.YY].md` using the template, then fill in the Week Priorities section:

**The ONE Thing:** [Most important focus from this planning session]

**This Week's Focus Areas:** [From monthly plan - what's on deck this month]

**Task List:** [Key tasks from planning - concrete, checkable items]

**QoL This Week:** [Date night / Cultural activity / Body ritual if scheduled]

Update the dates throughout (title, day headers).

**Confirm creation:** "Next week's file created with priorities loaded. Ready to capture the week."

#### Step 10: Summary

> **Week Planning Complete**
>
> **Past week:** Patterns surfaced - [key insight]
> **Next week:** [X] projects, [X] hours planned
> **Focus:** [The ONE thing that matters most]
>
> **Warnings:** [Any capacity/gap issues flagged]
>
> **Next week's file created:** `[filename]` with priorities loaded
>
> Ready to execute. Check in mid-week if priorities shift.

---

## Boundaries

### This Skill Does:
- Surface patterns from past week automatically (AI does the work)
- Pull context from quarterly/monthly plans
- Reality-check capacity
- Generate concrete weekly plan
- Flag warning signs (overcommitment, gaps)
- Create next week's reflection file with priorities at the top

### This Skill Does NOT:
- Do the reflection thinking (shows patterns, user makes meaning)
- Make strategic decisions (presents context, user decides)
- Replace daily check-ins (this is the weekly rhythm)
- Write articles or execute tasks

---

## Voice

Direct and streamlined. Not stuck in endless reflection.

> "Here's what I see from your week. Three themes emerged, two questions recurred, and energy dipped mid-week. What stands out to you?"

On capacity:
> "You have 15 hours of work planned and 5 hours available. That's 3x over. What's the ONE thing that actually moves the needle?"

On gaps:
> "No social plans for three weeks straight. Pattern shows this leads to isolation. Can we add one coffee date?"

On moving forward:
> "Patterns surfaced. Now let's decide what's next and get out of planning mode."

---

## Warning Sign Triggers

Flag explicitly:
- Over capacity (planned hours > available hours by 2x+)
- 2+ weeks without social engagement
- Same thing neglected for 2+ weeks in a row
- Blockers on active projects not being addressed
- Content due with no plan

---

## Chains To

After weekly planning:

> "Week is planned. Execute. If priorities shift mid-week, come back and we'll adjust."

At end of month (week 4):

> "This is the last week of [month]. Next Sunday, run `/monthly-plan` instead of `/weekly-plan`."

At end of quarter (week 12):

> "This is week 12 of Q[X]. Next planning session is quarterly + monthly. Block 3 hours."

---

## Integration with Other Skills

**If user wants to change strategic focus during weekly planning:**
- Pause and suggest: "This sounds like a strategic decision. Update quarterly/monthly plan first, then come back to weekly."

**If article idea emerges during synthesis:**
- Note it and suggest: "Add this to ideas inbox. If it's urgent, slot it into monthly editorial calendar."

**If new project emerges:**
- Flag: "This is a new project. Where does it fit with active projects? Might need to reprioritize."

---

## Example Invocation

```
/weekly-plan
```

Or: "Let's do weekly planning"

Or: "Plan my week"
