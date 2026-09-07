# Hermes Wingtips #59: a rate limit doesn't have to stop your session

posted 2026-08-31. original: [https://x.com/witcheer/status/2094362454390129137](https://x.com/witcheer/status/2094362454390129137)

Hermes Wingtips #59: a rate limit doesn't have to stop your session

Hermes Agent can carry a fallback chain: backup provider:model pairs it switches to automatically when your main model hits a rate limit, a server error or an auth failure.

~ hermes fallback

opens the same picker as hermes model. add as many backups as you want, they are tried in order.

history, tool calls and context all carry over, the agent continues from where it stopped. and it's per turn, your next message starts back on your primary.

one last tips: pin a local model last and no provider outage can fully stop you!
