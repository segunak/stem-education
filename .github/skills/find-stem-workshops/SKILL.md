---
name: find-stem-workshops
description: Find, verify, and maintain free browser-based STEM workshops for workshops/stem-workshops.md. Use this skill to search the web, Hacker News, and Reddit for zero-login STEM workshops and check activity links.
---

# Find STEM Workshops

## Context Setup

1. Read `workshops/stem-workshops.md` to prevent duplicates.
2. Read `.github/instructions/stem-workshops.instructions.md` and obey all eligibility and format rules.

## Search Sources

- Search for technology, coding, AI, and engineering workshops unless the user asks for another STEM subject.
- Find browser activities that a learner can start immediately on a career fair laptop.
- Use the links below as starting points only. Do not limit your search to these sites.
- Search across the open web for lesser-known workshops from independent creators, universities, museums, labs, and open-source projects.
- Check [Hacker News](https://news.ycombinator.com/), [Show HN](https://news.ycombinator.com/show), and [HN Search](https://hn.algolia.com/).
- Check [Reddit](https://www.reddit.com/) communities such as [r/CSEducation](https://www.reddit.com/r/CSEducation/), [r/STEM](https://www.reddit.com/r/STEM/), [r/edtech](https://www.reddit.com/r/edtech/), [r/ScienceTeachers](https://www.reddit.com/r/ScienceTeachers/), [r/Teachers](https://www.reddit.com/r/Teachers/), and [r/InternetIsBeautiful](https://www.reddit.com/r/InternetIsBeautiful/).
- Check directories such as [Hour of AI and Hour of Code](https://hourofai.org/en-US/activities), [Microsoft MakeCode](https://www.microsoft.com/en-us/makecode), [Raspberry Pi Projects](https://projects.raspberrypi.org/en/projects), and [PhET Simulations](https://phet.colorado.edu/).
- Include workshops from different providers instead of many workshops from one platform.

## Parallel Subagents

- Start subagents in parallel when you search multiple sources or topics.
- Use at least one subagent for open-web searches outside the listed sites to find lesser-known workshops.
- Give each subagent one source or topic, and require direct activity URLs in the results.

## Access Verification

1. Find the direct student start URL, not a forum post, blog post, or landing page.
2. Open each candidate URL with a browser tool when available.
3. Make sure that the activity starts without a login wall, class code, paywall, or software installation.
4. If no browser tool is available, check official pages and mark the workshop as untested in a browser.
5. Check the provider name, age range, and educator guide URL on official pages.

## Review Process

- Show verified workshops in chat in the exact list format.
- Wait for user approval before you change `workshops/stem-workshops.md`.
