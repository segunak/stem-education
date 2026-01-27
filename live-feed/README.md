# Live Feed

A simple live posts feed site for STEM workshops. Students prove they can write code to hit a live endpoint by submitting posts programmatically. Posts appear on a shared screen in near real-time.

**Live URL:** `https://stem.segunakinyemi.com/live-feed/`

## Why This Exists

During workshops I often want students to do something like:

- "Write code that POSTs your name and a message to this endpoint"
- "Share what your script discovered"
- "Post your AI prompt"

This creates a shared space where students submit via code (not a web form, unless that becomes relevant at some point) and see results live. No accounts, no API keys for students, no custom backend.

## How It Works

1. **Airtable** stores submissions in a table called `Posts`
2. **Students write code** (Python, JavaScript, or PowerShell) to POST to the Airtable form endpoint
3. **This page** embeds the Airtable view and auto-refreshes every 10 seconds when "Live Mode" is on
4. **Form password** gates submissions. Students get it verbally during the workshop.

## Page Features

- Tabbed code examples (Python, JavaScript, PowerShell) with real endpoint URLs
- Live Mode toggle (auto-refresh only when enabled AND tab is visible)
- Manual refresh button
- Password note telling students to ask instructor

## Airtable Setup

**Base:** <https://airtable.com/appC0ZE44OOVEtRsQ/tblIo9KaIf1rZ49fm/>

**Fun fact:** I believe that `cinnamon-rolls-are-the-best-pastry-hands-down`. This is a hill I will die on. That fact, in that exact format, might come in handy when trying to submit the form!

**Table:** `Posts` with fields:

- `Name` (required)
- `Message` (required)
- `Tags` (optional)
- `Created` (auto timestamp)

**Form:** Password-protected. Share password verbally during workshop.

**View:** `Live Feed` sorted by Created descending.

## Workshop Usage

**Before:**

1. Clear old posts or filter view to today's date
2. Open page on projector, enable Live Mode

**During:**

1. Share the page URL with students
2. Give them the form password verbally
3. Have them write code to submit posts

**After:**

- Export posts from Airtable if needed
- Clear rows for next session
