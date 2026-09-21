# Hermes Autopilot #6: a daily brief on the topics you name

posted 2026-09-18. original: [https://x.com/witcheer/status/2100954266038829170](https://x.com/witcheer/status/2100954266038829170)

this prompt gives your Hermes Agent a morning routine: a brief on the topics you follow, a source link on every line, at the time you pick, every day. paste it into a fresh chat and answer two questions.

paste this into a fresh Hermes Agent chat:

```
<role>
You are setting up a daily brief for me inside Hermes Agent. Ask, do not assume.
</role>

<principles>
<principle name="a source on every line">
Every line of the brief ends with the link it came from. A finding with no link is left out.
</principle>
<principle name="my topics, my words">
Follow the topics exactly as I give them. Do not add related topics on your own.
</principle>
<principle name="show before you create">
Nothing is created until I say yes. If you cannot get my answer, end your turn and create nothing.
</principle>
</principles>

<instructions>
1. Ask me for three to five topics to follow. One question, then wait for my reply.
2. Ask when and where the brief should arrive, then wait.
3. Search each topic once and show me a sample brief: one line per finding, the link at the end of the line, ten lines at most.
4. Show me the exact scheduled job you would create: its name, its schedule, the prompt it runs and where it delivers. Then stop and wait for my yes.
5. After my yes, create the job with your cron tool and tell me the command that lists it and the command that removes it.
</instructions>

<task>
Start with question one now.
</task>
```
