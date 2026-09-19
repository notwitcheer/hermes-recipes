# Hermes Wingtips #77: display.bell_on_complete + bell_on_prompt, a bell when Hermes finishes or needs you

posted 2026-09-19. original: [https://x.com/witcheer/status/2101229280185270718](https://x.com/witcheer/status/2101229280185270718)

you give Hermes Agent a long task in the CLI and switch to something else. while you are away it either finishes, or it stops to ask you something, an approval, a clarifying question, a sudo password, and waits.

either way you find out when you come back and look.

these two keys tell you instead. 

`bell_on_complete` rings the terminal bell when a turn finishes. `bell_on_prompt` rings it the moment a blocking prompt opens. both work over SSH, so a Hermes running on a server rings in the terminal on your desk. in Ghostty, iTerm2, Kitty and WezTerm the same keys also raise a desktop notification.

hermes config set display.bell_on_complete true
hermes config set display.bell_on_prompt true

both are off by default and read at startup, so restart the CLI after setting them.

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
