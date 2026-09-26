# Hermes Wingtips #83: approvals.denial_breaker_threshold, the smart-approval denial breaker

posted 2026-09-25. original: [https://x.com/witcheer/status/2103395194963980527](https://x.com/witcheer/status/2103395194963980527)

when the smart-approval reviewer denies a command, Hermes Agent can try a variation of it.

this key counts those denials in a row, per session. at 3, the deny message tells the agent to stop, report what was blocked, and ask you to run it yourself or /approve it.

lower it to stop sooner, or set 0 to turn it off.

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/configuration#denial-circuit-breaker](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#denial-circuit-breaker)
