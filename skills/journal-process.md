---
name: journal-process
description: Process voice journal recordings from Granola or similar. Use when you say "process this recording", "clean up this journal", "journal process", or "/journal-process".
---

# Journal Process

## Purpose
Take voice journal recordings (typically from Granola) and transform them into clean, structured entries for your weekly reflection file. Cleans up speech artifacts while preserving your voice, extracts natural structure from the content, and appends to the appropriate day.

## When to Use
- "process this recording"
- "clean up this journal"
- "journal process"
- `/journal-process`
- When you paste a Granola transcript or recording output

## Input Format
Granola typically outputs:
1. An AI-generated summary at the top
2. The raw transcript below

The skill works with either or both.

## Files This Skill Reads
- Current week's reflection file (to find the right day section and match existing style)
- **Customize:** Update the path to match your vault structure

## Files This Skill Writes
- Appends to the current week's reflection file under the specified day

---

## The Process

### Step 1: Get the Recording
Ask user to paste the Granola output (or accept if already pasted).

```
> Paste your Granola recording and let me know which day this is for.
```

If the day isn't specified, ask:
```
> Which day is this for? (e.g., "Thursday" or "01.23.26")
```

---

### Step 2: Clean the Transcript

**Remove:**
- Filler words (um, uh, like, you know, sort of, kind of, I mean, basically, literally, right?)
- False starts and repetitions
- Verbal stutters

**Fix:**
- Grammar and punctuation
- Run-on sentences (break into readable chunks)
- Obvious transcription errors

**Preserve:**
- Natural voice and phrasing
- Conversational asides and tangents (these are often valuable)
- The authentic feel of spoken reflection

**Do NOT:**
- Over-polish into formal writing
- Add content that wasn't said
- Remove personality or edge
- Sanitize opinions or frustrations

---

### Step 3: Infer Structure

Look at what was talked about and create natural sections. Don't force a template.

**If the content has clear topics:**
```markdown
## Morning Workout

[content about the workout]

## Work: The Project Update

[content about work]

## Evening Reflection

[content about evening]
```

**If it's stream-of-consciousness:**
Keep it as flowing paragraphs with minimal headers.

**Common section patterns:**
- `## Morning/Energy` - how you woke up, physical state
- `## Work: [Specific Topic]` - work-related with specificity
- `## [Topic] Frustration` - when processing something annoying
- `## The Big Thing` - significant realization or event
- `## Evening/Social` - end of day, social interactions

---

### Step 4: Extract Key Elements

At the end of the cleaned content, add (only if relevant):

**Key Takeaways** (if there are clear insights):
```markdown
### Key Takeaways
- [Insight or realization]
- [Pattern noticed]
```

**Action items** (if mentioned):
```markdown
### To Do
- [ ] [Thing mentioned as needing to be done]
```

Skip these sections entirely if nothing fits.

---

### Step 5: Show Draft for Approval

Before writing to the file, show the cleaned version:

```
> Here's the cleaned journal entry for [Day]:
>
> [formatted content]
>
> Ready to add this to your weekly reflection?
```

---

### Step 6: Append to Weekly Reflection

Once approved, find the current week's file and add under the appropriate day.

---

## Boundaries

**This skill DOES:**
- Clean up speech-to-text artifacts
- Structure content based on natural topics
- Preserve voice and opinions
- Append to existing weekly reflection files

**This skill does NOT:**
- Create new files
- Add content that wasn't said
- Over-polish or formalize the writing
- Remove personality, edge, or frustration
- Process content without showing a draft first

## Voice
Clean but authentic. The goal is readability, not perfection. Reflections should sound like you, just without the "um"s.

## Chains To
- After processing, offer: "Want me to run `/daily-process` to file any loose notes in your vault?"
- On Sunday, might chain to `/weekly-plan`

---

## Customization

To use this skill, update these paths to match your setup:
- Weekly reflection file location
- The day header format you use (e.g., `# Monday 01.20.26`)
- Any specific sections you want in your reflections
