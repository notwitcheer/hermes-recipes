# Hermes Autopilot #2: turn what you just did into a skill

posted 2026-09-10. original: [https://x.com/witcheer/status/2098058859189277008](https://x.com/witcheer/status/2098058859189277008)

finished a task with your Hermes Agent that you will need again? paste this prompt into the same chat. it reads the session back, drafts a SKILL.md from the steps that actually worked, shows it to you and waits. it saves only on your yes.

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent. We just finished a piece of work together in this session. Turn what we did into a skill, so the next time it is a procedure and not a memory. Ask, do not guess.
</role>

<principles>
<principle name="Show before you write">
Draft the whole skill and show it to me. Nothing is saved until I say yes.
</principle>
<principle name="Only what we did">
The steps are the ones that worked in this session, in the order they worked. No steps you did not run, no invented commands.
</principle>
<principle name="Trigger first">
The description line opens with when to use the skill, in under sixty characters. That line is what you read when you decide to pick a skill on your own.
</principle>
</principles>

<instructions>
1. Read back this session. Name the task we did, in one sentence.
2. Draft a SKILL.md: name, description, when to use, the steps that worked, the pitfalls we hit and how we got past them.
3. Keep it under forty lines.
4. Show me the draft and wait.
5. On my yes, save it with your skill tool and tell me the path.
</instructions>

<task>
Start with step one now.
</task>
```
