# Hermes Wingtips #62: cron.model

posted 2026-09-04. original: [https://x.com/witcheer/status/2095722000907923465](https://x.com/witcheer/status/2095722000907923465)

Hermes Wingtips #62: cron.model

your scheduled jobs and your chat sessions do not have to share a model. without a cron setting, a new job runs on your global default, the same model you chat with, even when the task is a small daily digest.

two ways to route cron spend:

(1) `hermes config set cron.model \<model\>`

a fleet default: every job without its own pin runs on this model.

(2) `hermes cron edit \<job_id\> --model \<model\> --provider \<provider\>`

a per-job pin, for when one heavy scheduled analysis deserves the big model while the rest run cheap.

super useful if you run digests, watchers or reminder jobs 24/7: keep the flagship for conversations and let a smaller model do the routine rounds!
