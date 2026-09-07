# Hermes Wingtips #47: cron prompts

posted 2026-08-17. original: [https://x.com/witcheer/status/2089275668949356763](https://x.com/witcheer/status/2089275668949356763)

Hermes Wingtips #47: cron prompts

your agent nails a task in chat, you schedule the same thing with /cron, and the scheduled runs come back wrong.

the reason is simple: a cron job runs in a fresh session, with none of the chat context that made the task work. a prompt leaning on what you discussed earlier has nothing to lean on at run time.

so write the prompt like the agent has never met you: every url, every command, every rule spelled out inside the prompt itself.

this is also why a scheduled job cannot ask you clarifying questions, it answers with what the prompt gave it!
