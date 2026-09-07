# Hermes Wingtips #16: gateway won't restart after a reboot? enable lingering

posted 2026-07-08. original: [https://x.com/witcheer/status/2074942527996838105](https://x.com/witcheer/status/2074942527996838105)

Hermes Wingtips #16: gateway won't restart after a reboot? enable lingering

a user-service gateway runs under your login, so it stops at logout and won't come back after a reboot until you enable lingering.

headless VPS, zero root per restart:

```
hermes gateway install
sudo loginctl enable-linger $USER
```

or go boot-level: `sudo hermes gateway install --system`
