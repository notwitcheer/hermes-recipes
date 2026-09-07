# Hermes Wingtips #6: if your Hermes box fills its disk, it's likely not the logs

posted 2026-06-25. original: [https://x.com/witcheer/status/2070141757707239594](https://x.com/witcheer/status/2070141757707239594)

Hermes Wingtips #6: if your Hermes box fills its disk, it's likely not the logs. 

the unbounded growers are state-snapshots (750MB on mine), per-run cron output (1,500+ files), and stdout if your host pipes it to a file. 

run the disk-cleanup plugin and watch those three before the "no space left" crash.
