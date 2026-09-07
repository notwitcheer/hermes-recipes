# Hermes Wingtips #1: running a hermes agent in a telegram group and it just sits there silent?

posted 2026-06-18. original: [https://x.com/witcheer/status/2067717599090143569](https://x.com/witcheer/status/2067717599090143569)

Hermes Wingtips #1

running a hermes agent in a telegram group and it just sits there silent? 
the usual cause is BotFather's group privacy mode: it's on by default, so the bot only sees messages that mention it or start with /. 

plain group messages never reach it.

easy fix: message BotFather, /setprivacy, pick the bot, Disable.

it doesn't apply to groups the bot is already in. remove it from the group and re-add it for the change to take.
