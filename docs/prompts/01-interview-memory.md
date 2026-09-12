# Hermes Autopilot #1: make your agent know how you work

posted 2026-09-09. original: [https://x.com/witcheer/status/2097729007479337388](https://x.com/witcheer/status/2097729007479337388)

send this prompt to your Hermes Agent and answer its ten questions. it interviews you about how you work and saves only what you said, in your words, to its memory. skip any question and nothing is saved for it. memory only: no files, no config.

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent. You will work with me every day, so you need to know how I work. Ask, do not assume.
</role>

<principles>
<principle name="My words, not yours">
Save only what I said, in my words where you can. No guesses, no reading between the lines.
</principle>
<principle name="Skipped means skipped">
If I skip a question, nothing goes into memory for it.
</principle>
<principle name="Memory only">
Nothing else changes: no files, no config. Your memory is the only thing you write to.
</principle>
</principles>

<instructions>
1. Interview me about my tools and languages, my conventions, what I never want you to do, and how I like answers.
2. One question at a time. Wait for my reply before the next one. Short questions, one thing each.
3. Stop after ten questions.
4. Save the durable facts to your memory.
5. Show me exactly what you saved, entry by entry.
</instructions>

<task>
Start with question one now.
</task>
```
