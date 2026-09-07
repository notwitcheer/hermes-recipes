# Hermes Wingtips #22: steer a task without stopping it

posted 2026-07-16. original: [https://x.com/witcheer/status/2077799836804407715](https://x.com/witcheer/status/2077799836804407715)

Hermes Wingtips #22: steer a task without stopping it

a lot of people think you have to stop the agent and start over to change direction mid-task. you don't. there is /steer.

while it works, send a mid-run note: 

`/steer focus on the auth module first`

it arrives after the current tool call finishes, so nothing gets interrupted and it is not a new turn, just fresh direction the agent picks up as it goes.

two siblings worth knowing: 

(1) /queue (alias /q) holds a prompt for the next turn without touching the current one

(2) /busy lets you set what plain Enter does while it works: queue, steer, or interrupt.
