# Hermes Wingtips #50: the [SILENT] marker

posted 2026-08-21. original: [https://x.com/witcheer/status/2090697512097112274](https://x.com/witcheer/status/2090697512097112274)

Hermes Wingtips #50: the [SILENT] marker

a monitoring job that reports every run trains you to ignore it. your Hermes Agent has a quieter contract: if a cron job's response contains [SILENT], delivery is suppressed and nothing lands in your chat.

the lever is the prompt itself:

"check if nginx is running. if everything is healthy, respond with only [SILENT]. otherwise, report the issue."

great for any check that should only speak up when something is wrong: uptime, disk space, backups, feed watchers!
