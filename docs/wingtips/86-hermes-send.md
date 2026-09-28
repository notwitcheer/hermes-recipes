# Hermes Wingtips #86: hermes send, message your chats from any script

posted 2026-09-28. original: [https://x.com/witcheer/status/2104531742686093765](https://x.com/witcheer/status/2104531742686093765)

one command sends a message from any script to the platforms your Hermes Agent is already set up on.

it uses your gateway's bot credentials and makes no model call.

`hermes send --to telegram "deploy finished"`

or pipe anything into it:

`tail -n 20 build.log | hermes send --to telegram`

useful in cron scripts, CI jobs, or as a ping when a long training run is done!

docs: [https://hermes-agent.nousresearch.com/docs/guides/pipe-script-output](https://hermes-agent.nousresearch.com/docs/guides/pipe-script-output)
