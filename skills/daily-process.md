---
name: daily-process
description: Process unfiled notes and surface daily observations. Use at end of day or when you say "process the day", "daily processing", or "organize my notes".
---

# Daily Process

## Purpose
End-of-day note hygiene and pattern surfacing. This skill finds notes that haven't been filed, adds proper metadata, moves them to the right folder, and surfaces observations about what's on your mind based on what you captured.

## When to Use
- "process the day"
- "daily processing"
- "organize my notes"
- End of day when you want to close loops on captured notes

## Files This Skill Reads
1. All `.md` files in your vault root (unfiled notes)
2. Note content to determine classification and tags

## Files This Skill Writes/Updates
- Moves notes to appropriate folders:
  - `Fleeting/` - Raw thoughts, fragments, quick captures
  - `Literature/` - Notes about external content (books, articles, podcasts)
  - `Ideas/` - Developed thinking, concepts, synthesis
- Adds/updates YAML front matter on each note

---

## The Process

### Step 1: Scan for Unfiled Notes
Find all `.md` files in the vault root that are not in organized folders.

```
> "Let me scan your vault for unfiled notes..."
```

**Output:** List of unfiled notes found

**If no unfiled notes:** Skip to Step 5 and reflect on the day without file processing.

---

### Step 2: Classify Each Note

For each unfiled note, read the content and determine:

#### Folder Assignment
- **Fleeting**: Raw thoughts, quick captures, fragments, questions without answers, brain dumps, no clear structure
- **Literature**: References external content - books, articles, podcasts, videos, quotes from others, things consumed
- **Ideas**: Developed thinking, concepts being explored, synthesis of multiple ideas, has some structure

#### Tag Inference
Scan content for domain signals and assign relevant tags based on your interests.

#### State Assignment
- `seed` - Very rough, just a question or fragment, placeholder
- `sprout` - Has some substance but undeveloped, emerging idea
- `leafing` - Has structure, emerging ideas, being actively developed

---

### Step 3: Add YAML Front Matter

For each note, add or update front matter:

```yaml
---
title: [filename without extension]
date_created: [today's date YYYY-MM-DD]
tags:
  - [type tag: fleeting/literature/idea]
  - [domain tag(s) inferred from content]
state: [seed/sprout/leafing]
publish: false
---
```

**If front matter exists:** Preserve existing values, only add missing fields.

---

### Step 4: Move to Correct Folder

Move each note to its determined folder:
- Fleeting notes → `Fleeting/`
- Literature notes → `Literature/`
- Idea notes → `Ideas/`

```
> "Moving [note title] to [folder]..."
```

---

### Step 5: Daily Reflection

After processing (or if no notes to process), share observations in chat:

```
> **Daily Processing Complete**
>
> **Notes processed:** [count]
> - [note title] → [folder] (tags: [tags])
> - ...
>
> **Patterns I notice:**
> [What themes emerged across today's notes? What's on your mind?]
>
> **Observation:**
> [One reflection on what these notes suggest about where your attention is]
```

This reflection is conversational and ephemeral - it does NOT get saved to a file.

---

## Boundaries

**This skill DOES:**
- Process notes in the vault root only
- Add missing front matter
- Move notes to appropriate folders
- Surface patterns conversationally

**This skill does NOT:**
- Touch notes already in organized folders
- Create permanent reflection files
- Modify existing front matter values (only adds missing fields)
- Process non-markdown files
- Reorganize the folder structure

## Voice
Direct, observational. Like a thoughtful assistant helping you close out the day. No excessive commentary - just what was done and what patterns emerged.

## Chains To
- This skill should be **chained from other skills** to ensure it gets used:
  - After `/weekly-plan`: "Did you run `/daily-process` this week?"
  - After `/journal-process`: "Want me to file any loose notes?"

---

## The Chaining Lesson

**Important:** This skill was created and then forgotten for months because it had no external trigger.

Skills for personal productivity need hooks:
1. A trigger in your existing routine (calendar, habit, chain from another skill)
2. To be few enough that you remember they exist

If you build this skill, make sure to chain it to something you already do regularly.

---

## Customization

To use this skill, update:
- Vault root path
- Folder names (Fleeting, Literature, Ideas) to match your structure
- Tag categories to match your domains
- State labels if you use different terminology
