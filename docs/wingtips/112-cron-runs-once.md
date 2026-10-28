# Hermes Wingtips #112: a scheduled job that runs once

posted 2026-10-28. original: [https://x.com/witcheer/status/2115428373564375354](https://x.com/witcheer/status/2115428373564375354)

start the schedule with "in" and the job runs one time:

`hermes cron create "in 2h" "Remind me to call the dentist before they close."`

your gateway runs it once, two hours from now, and the job then clears itself from your list. "in 30m" and "in 1d" work the same way.

handy for a call to return, a parcel to chase or a build to check later today!

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/features/cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
