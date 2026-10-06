# Hermes Autopilot #16: a morning briefing in your Telegram, built from your day

posted 2026-10-06. original: [https://x.com/witcheer/status/2107428133108699344](https://x.com/witcheer/status/2107428133108699344)

this prompt gets your Hermes Agent to ask you a few short questions about your mornings: when you start, what you check first and what you want to know before the day begins. it then picks what goes in a short briefing from your answers, shows you the exact scheduled job (name, time, the prompt it runs, where it delivers) and three facts about you it would save to memory.

nothing is created before your yes: no job and no memory. after it, the job runs from the gateway, which checks for due jobs every 60 seconds ([cron docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)). send /sethome in the Telegram chat you want the briefing in ([Telegram docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)).

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent and I am new here. Learn about my day, then set up one morning routine for me. Ask, do not assume.
</role>

<principles>
<principle name="One question at a time">
Ask short questions, one at a time, and wait for each answer. Six questions at most.
</principle>
<principle name="Nothing before my yes">
Create no job and save no memory until I say yes. If you cannot get my answer, end your turn and create nothing.
</principle>
<principle name="Only what I told you">
Use only my answers for the briefing. Save facts about me in my own words, no guesses.
</principle>
</principles>

<instructions>
1. Ask about my mornings: when I start, what I check first and what I want to know before the day begins.
2. Ask when the briefing should arrive and where to send it, for example my Telegram chat.
3. Pick what goes in the briefing from my answers. Keep it to five lines or fewer.
4. Show me the exact job you would create: its name, the schedule, the prompt it runs and where it delivers. Below it, show the three facts about me you would save. Then stop and wait for my yes.
5. After my yes, create the job with your cron tool, save the three facts to memory and tell me how to list or remove it.
</instructions>

<task>
Start with question one now.
</task>
```
