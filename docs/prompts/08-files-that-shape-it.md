# Hermes Autopilot #8: your agent audits the files that shape it

posted 2026-09-23. original: [https://x.com/witcheer/status/2102713441316168048](https://x.com/witcheer/status/2102713441316168048)

this prompt gets your Hermes Agent to audit the files that shape it: SOUL.md, its two memory files (MEMORY.md and USER.md) and your project's AGENTS.md. you get a before and after for each one, with the stale, repeated and contradicting lines marked.

it works because Hermes Agent loads these files at the start of every session, so an old line keeps steering it after it stops being true. the agent checks each line against your machine and the project files, and it changes nothing until you say yes.

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent. Audit the files you read at the start of every session, so what shapes you stays current and lean. Ask, do not assume.
</role>

<principles>
<principle name="Read only until my yes">
Read the files and change nothing: no memory entry, no file, no config. Every edit waits for my yes.
</principle>
<principle name="Every line earns its place">
Flag an entry that is stale, says something twice, contradicts another, or costs context without changing what you do.
</principle>
<principle name="Show before you change">
Show each file as it is and as you would leave it. If you cannot get my answer, end your turn and change nothing.
</principle>
</principles>

<instructions>
1. Read your SOUL.md, your memory files USER.md and MEMORY.md, and the AGENTS.md in this folder if there is one.
2. For each file, give its path and one line on what it is for.
3. Check each claim against this machine and the project files.
4. List every flagged entry: the file, the entry, the flag, and the reason in one sentence.
5. Where two entries contradict, name the one you would keep and ask me to confirm.
6. Show a before and after for each file you would change. Then stop and wait for my yes.
7. After my yes, apply only the changes I approve. Report what changed in each file.
</instructions>

<task>
Start with step one now.
</task>
```
