# Hermes Wingtips #40: give your local agent two commands, not root

posted 2026-08-07. original: [https://x.com/witcheer/status/2085640740353233270](https://x.com/witcheer/status/2085640740353233270)

Hermes Wingtips #40: give your local agent two commands, not root

when I'm running benchmarks, my local Hermes Agent stops and starts the model server on its own, from cron, with no password. it still cannot touch anything else as root.

the trick is a sudoers rule scoped to exactly one service: NOPASSWD applies to systemctl start and stop for that unit, nothing more.

still test the fence from the outside: sudo -n on any other service should still ask for a password.
