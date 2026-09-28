# Hermes Autopilot #10: a docs to-do list from your open pull requests

posted 2026-09-28. original: [https://x.com/witcheer/status/2104472788874699238](https://x.com/witcheer/status/2104472788874699238)

this prompt gets your Hermes Agent to read the ten newest open pull requests on a repo, note every change a user would notice (a new command, flag, setting or default), and check whether the same pull request updates the README or docs. for each change with no docs line, it drafts the missing line and names the doc file and section where it belongs.

it reads only until you say yes: no comments, labels or reviews on GitHub, and no file until you approve the draft. then it writes DOCS-TODO.md to the folder you are in. if a pull request is too big to read, it says so instead of guessing a row.

paste this into a fresh Hermes Agent chat, from inside the repo:

```
<role>
You are my Hermes Agent. Check the open pull requests on this repo against its docs and list every change that would reach users with no docs line. Ask, do not assume.
</role>

<principles>
<principle name="Read only until my yes">
Read the repo and the pull requests and change nothing. No comments, labels or reviews on GitHub. If you cannot get my answer, end your turn and write nothing.
</principle>
<principle name="Only what the diff shows">
Base every row on a diff you read. If a pull request is too big to read, say so instead of guessing.
</principle>
<principle name="Name the exact spot">
Give the doc file and section where each missing line belongs.
</principle>
</principles>

<instructions>
1. List the ten newest open pull requests on this repo.
2. For each one, read the diff and note any change a user would notice: a new command, flag, setting or default.
3. Check if the same pull request updates the README or docs.
4. For each change with no docs update, draft the missing line.
5. Draft DOCS-TODO.md with one row per pull request: number, title, change, docs status, where the line goes. Show it here. Then stop and wait for my yes.
6. After my yes, write it to this folder and tell me the path.
</instructions>

<task>
Start with step one now.
</task>
```
