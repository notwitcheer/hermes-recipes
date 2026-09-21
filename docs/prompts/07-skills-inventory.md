# Hermes Autopilot #7: a skills inventory your agent writes for you

posted 2026-09-21. original: [https://x.com/witcheer/status/2102053116178825319](https://x.com/witcheer/status/2102053116178825319)

this prompt gets your Hermes Agent to write the list of everything it can do: every skill installed, one line each, what it does in plain words and where it lives.

it works because skills are files on your disk. each one is a folder with a SKILL.md, and the agent opens every one of them itself: it rewords each description, checks the body against it, and looks for two skills doing the same job. the result is skills-index.md, a file you can open.

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent. Write an inventory of every skill installed for you, so I can see what you can do and what is cluttering the tree. Ask, do not assume.
</role>

<principles>
<principle name="Read only until my yes">
Read the skills tree and nothing else changes: no skill edited or removed, no config touched. The only thing you ever write is the one file I ask for.
</principle>
<principle name="Plain words, one line each">
One line per skill: its name, what it does in plain words, and where it lives. Reword the description; do not paste it.
</principle>
<principle name="Show before you write">
Show me the whole index and wait. Write the file only on my yes. If you cannot get my answer, end your turn and create nothing.
</principle>
</principles>

<instructions>
1. List your skill roots: your skills folder and any profile or plugin roots you can see. Give the path of each.
2. Read every SKILL.md under those roots. List every skill on one line: name, what it does, where it lives.
3. Flag overlaps: two or more skills covering the same job. Flag skills whose description does not match what the body does.
4. For each flagged skill, propose one word: keep, merge or remove. Give the reason in one sentence.
5. Show me the index and the flags. Then stop and wait for my yes.
6. After my yes, ask me where to save it if I have not said, and write it as skills-index.md there. Report the path and how many lines it has.
</instructions>

<task>
Start with step one now.
</task>
```
