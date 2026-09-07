# Hermes Wingtips #48: platform toolsets

posted 2026-08-18. original: [https://x.com/witcheer/status/2089706892993941840](https://x.com/witcheer/status/2089706892993941840)

Hermes Wingtips #48: platform toolsets

your agent pays a fixed token overhead before it reads a single word of your message, and one of the biggest slice is not the prompt.

every tool your platform loads ships its full schema with every call, used or not. 

if a session never touches the browser, image gen or TTS, `platform_toolsets` in config.yaml hands that platform a smaller set.

`hermes prompt-size` shows you the before and after without spending a token.
