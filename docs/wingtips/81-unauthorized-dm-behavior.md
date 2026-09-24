# Hermes Wingtips #81: unauthorized_dm_behavior, what your bot says to someone you have not approved

posted 2026-09-23. original: [https://x.com/witcheer/status/2102680195161366668](https://x.com/witcheer/status/2102680195161366668)

when someone you have not approved messages your Hermes bot, it answers with a one-time pairing code, so you can let them in from the CLI.

new in Hermes Agent: if the bot is only for you, it can say no instead.

`unauthorized_dm_behavior: decline`

one short, polite decline, then silence toward that sender for a day.

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/configuration#unauthorized-dm-behavior](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#unauthorized-dm-behavior)
