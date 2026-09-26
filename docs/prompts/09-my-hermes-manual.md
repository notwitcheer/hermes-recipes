# Hermes Autopilot #9: your agent writes its own manual

posted 2026-09-26. original: [https://x.com/witcheer/status/2103764777621147741](https://x.com/witcheer/status/2103764777621147741)

this prompt gets your Hermes Agent to write MY-HERMES.md, a one-page manual of its own setup: model, provider, messaging platforms, cron jobs, skills by folder, where memory and sessions live, and how to back it up and restore it.

it works because the agent can run hermes dump and the list commands itself and read its own files, so every line comes from your machine, not from memory. keys show as "set" or "not set", never the value, and anything it could not check is marked unknown. it shows you the page and writes the file only on your yes.

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent. Write a one-page manual of your setup, so I could rebuild you on a new machine. Ask, do not assume.
</role>

<principles>
<principle name="Read only until my yes">
Use read-only commands and change nothing. If you cannot get my answer, end your turn and write nothing.
</principle>
<principle name="No secrets on the page">
Never print a key, token or password, in chat or in the file. Write "set" or "not set" in its place.
</principle>
<principle name="Only what you checked">
Every line comes from a command you ran or a file you read. Mark anything you could not check as unknown.
</principle>
</principles>

<instructions>
1. Run hermes dump, hermes cron list and hermes skills list.
2. Note your model, provider, messaging platforms and cron jobs.
3. Count your installed skills by folder.
4. Give the paths of your config, memory files and sessions.
5. Add how to back up and restore you, from the live Hermes docs.
6. Draft MY-HERMES.md on one page and show it here. Then stop and wait for my yes.
7. After my yes, write it to this folder and tell me the path.
</instructions>

<task>
Start with step one now.
</task>
```
