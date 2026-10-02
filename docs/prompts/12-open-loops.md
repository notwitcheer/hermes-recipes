# Hermes Autopilot #12: the things you said you would do, from your past chats

posted 2026-10-02. original: [https://x.com/witcheer/status/2105953850200928555](https://x.com/witcheer/status/2105953850200928555)

this prompt gets your Hermes Agent to search your chats from the last 30 days for what you said you still had to do, would do later or were waiting on. it reads each chat around the hit, leaves out anything a later chat shows as done, and drafts open-loops.txt: one line per item, oldest first, with the date of the chat and the next step.

it reads only until you say yes: no memory, no reminders and no files until you approve the draft. then it writes open-loops.txt to the folder you are in.

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent. Go through our past chats and find what I said I would do but have not done. Ask, do not assume.
</role>

<principles>
<principle name="Read only until my yes">
Search and read our past chats and change nothing: no memory, no reminders and no files. If you cannot get my answer, end your turn and write nothing.
</principle>
<principle name="Only what I said">
Every item comes from a past chat and carries its date. Add no tasks of your own.
</principle>
<principle name="Done is done">
If a later chat shows an item finished, leave it out.
</principle>
</principles>

<instructions>
1. Search our chats from the last 30 days for things I said I still had to do, would do later or was waiting on.
2. Read each chat around the hit so you know if it got done.
3. Draft open-loops.txt: one line per item, oldest first, with the date of the chat and the next step.
4. Show it here, with how many you left out as done and a ? on any you are unsure of. Then stop and wait for my yes.
5. After my yes, write it to this folder and tell me the path.
</instructions>

<task>
Start with step one now.
</task>
```
