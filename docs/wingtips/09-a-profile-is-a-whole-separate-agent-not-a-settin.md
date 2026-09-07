# Hermes Wingtips #9: a profile is a whole separate agent, not a setting

posted 2026-06-30. original: [https://x.com/witcheer/status/2071924626561638757](https://x.com/witcheer/status/2071924626561638757)

Hermes Wingtips #9: a profile is a whole separate agent, not a setting

a Hermes profile is a second agent in its own right: its own memory, sessions, skills and bot token. spin one up and it knows nothing your main agent does. 

two things to understand:

(1) you want one agent across Telegram, Discord and WhatsApp? that's a single profile with several gateways: they share one SOUL.md and one memory, so it behaves as one agent everywhere. 

vice versa, a profile per platform splits it into strangers.

(2) you want a fresh agent that starts from your current one? hermes profile create new --clone-all. without it the new profile is blank.
