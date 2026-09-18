# Hermes Wingtips #76: display.vim_mode, vi keys in the Hermes CLI input box

posted 2026-09-18. original: [https://x.com/witcheer/status/2100853054970990803](https://x.com/witcheer/status/2100853054970990803)

the Hermes Agent CLI has an input box where you type your message to the agent. out of the box it uses the standard terminal editing keys.

if you type in vim all day, that box can use vi keys instead: Esc puts you in NORMAL mode, i takes you back to INSERT, and the status bar shows the mode you are in at its right edge.

set `display.vim_mode: true` in your config.yaml and restart the CLI.

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
