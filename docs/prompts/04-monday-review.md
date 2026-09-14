# Hermes Autopilot #4: the Monday review that writes itself

posted 2026-09-14. original: [https://x.com/witcheer/status/2099485722545648017](https://x.com/witcheer/status/2099485722545648017)

want a Monday morning note on what you and your Hermes Agent did last week, written by the agent itself? paste this prompt into a fresh chat. it searches your sessions from the last seven days, writes a ten-line review, and shows you the scheduled job before it exists: the day, the hour, the prompt it will run and where it lands. nothing is created until you say yes.

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent. Build me a weekly review that writes itself: every Monday morning, a short summary of what we worked on together the week before. Ask, do not assume.
</role>

<principles>
<principle name="Show before you schedule">
Draft the first review now from our past sessions and show it to me. Create the scheduled job only after I say yes. If you cannot get my answer, end your turn and create nothing.
</principle>
<principle name="Ten lines, not a report">
The review is ten lines at most: what we finished, what is still open, and one thing worth doing next. Plain words, no headings.
</principle>
<principle name="Only what is on record">
Use our session history and your memory. If the record is thin, say so instead of filling the gaps.
</principle>
</principles>

<instructions>
1. Search our sessions from the last seven days and list the topics you find, one line each.
2. Write the ten-line review from that list. Show it to me.
3. Ask me which day and time I want it, and where to deliver it.
4. Show me the exact job you would create: the schedule, the prompt it will run, and the delivery target. Then stop and wait for my yes.
5. After my yes, create the job and tell me its name and how to remove it.
</instructions>

<task>
Start with step one now.
</task>
```

where the review arrives: wherever you chat with your agent through the gateway (Telegram, Discord, Slack, Hermes Desktop). from a plain terminal session the job saves its output and you read it with `hermes cron list` or by asking the agent for the last review. the cron dials it leans on have their own Wingtips: [#55](../wingtips/55-chaining-cron-jobs.md) and [#62](../wingtips/62-cron-model.md).
