# Hermes Wingtips #82: agent.session_stall_timeout, the stall notice explained

posted 2026-09-24. original: [https://x.com/witcheer/status/2102997146660110386](https://x.com/witcheer/status/2102997146660110386)

if your Hermes bot has ever sent "Agent session appears stalled", that is a watchdog, and it never stops the turn.

it speaks up once when you have sent a follow-up and the agent has shown no activity for 5 minutes. then it is your call: /new, /stop, or keep waiting.

raise the number for long jobs, or set 0 to turn it off.

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/configuration#session-stall-watchdog](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#session-stall-watchdog)
