# release explainer #5: bot-to-bot messaging

posted 2026-09-05. original: [https://x.com/witcheer/status/2096174013332561939](https://x.com/witcheer/status/2096174013332561939)

since the Pantheon release here is how I use Hermes Agent bots: one agent sent a request to another profile's Bot Chat, finished its own turn, and the reply came back later as a notification, attributed to the sender.

how it works:

(1) every bot knows its teammates. the live roster, names and roles, is part of each Bot Chat, so a bot picks the right recipient on its own

(2) a bot messages another with the `message_agent` tool: the target is validated against the roster, the message lands in that bot's own Bot Chat with a "Message from" attribution, and the reply arrives when it has one

(3) you can also hand work off yourself: type "@ researcher have a look at this" in any chat and the active bot composes its own message to that bot. your text is never forwarded verbatim

this all works headless too: hermes -p <bot> chat opens the same canonical Bot Chat from the CLI, so a VPS fleet messages the same way a Desktop one does.

https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode
