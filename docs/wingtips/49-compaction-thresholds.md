# Hermes Wingtips #49: compaction thresholds

posted 2026-08-19. original: [https://x.com/witcheer/status/2090030442363670584](https://x.com/witcheer/status/2090030442363670584)

Hermes Wingtips #49: compaction thresholds

when your Hermes Agent stops mid-task to summarize, the number in that warning is not random. compaction fires at a fixed fraction of your main model's context window.

the fraction is `compression.threshold` in config.yaml, and it is always read off the model you chat with, never the summarizers' window.

on smaller context windows Hermes waits longer by default, so a compaction cannot fire with half the window still free.

and if you switch between a huge-context model and a small one, `compression.model_thresholds` sets a different trigger per model, matched on the model name.
