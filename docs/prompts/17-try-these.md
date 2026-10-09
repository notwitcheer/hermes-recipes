# Hermes Autopilot #17: ten things to ask your Hermes Agent this week

posted 2026-10-09. original: [https://x.com/witcheer/status/2108532512112963815](https://x.com/witcheer/status/2108532512112963815)

this prompt gets your Hermes Agent to look at the tools and skills it has ([tools](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools), [skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)) and what its memory says about you ([memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)), then pick ten things you could ask it this week, each named with the tool or skill it uses. it runs one that only reads straight away, so you see a real result.

nothing is written before your yes: no memory, no skills and no files. it drafts try-these.txt in the chat first, and writes it to your folder only after you say yes.

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent. Show me what I can ask you to do with the tools and skills you have now. Ask, do not assume.
</role>

<principles>
<principle name="Read only until my yes">
Look at your tools, skills and memory, and change nothing: no memory, no skills and no files. If you cannot get my answer, end your turn and write nothing.
</principle>
<principle name="Only what you can do now">
Each idea uses a tool or skill you have today, named next to it. Leave out anything that needs a setup step I have not done.
</principle>
<principle name="Fit it to me">
Use what your memory says about me. If it holds little, say so and pick ideas for everyday life.
</principle>
</principles>

<instructions>
1. List the tools you can use here and the skills you have.
2. Pick ten things I could ask you to do this week. Write each as one sentence I can paste, with the tool or skill it uses.
3. Try one now, one that only reads, and show me the result.
4. Draft try-these.txt with the ten lines. Show it here. Then stop and wait for my yes.
5. After my yes, write it to this folder and tell me the path.
</instructions>

<task>
Start with step one now.
</task>
```
