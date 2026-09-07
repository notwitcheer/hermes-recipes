# Hermes Wingtips #61: cron preflight

posted 2026-09-02. original: [https://x.com/witcheer/status/2095028256332271691](https://x.com/witcheer/status/2095028256332271691)

Hermes Wingtips #61: cron preflight

before a scheduled job runs, your Hermes Agent checks that the run can actually succeed: the provider key resolves, attached skills have what they need, delivery targets are reachable.

a job that fails the check is marked blocked_config and alerts you once. no model call happens, so it sits at zero cost until you fix it.

the next healthy run clears the state on its own.
