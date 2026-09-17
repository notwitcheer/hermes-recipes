# release explainer #9: the plugin catalog

posted 2026-09-17. original: [https://x.com/witcheer/status/2100532064550302181](https://x.com/witcheer/status/2100532064550302181)

here are the answers to the questions you asked most under yesterday's plugin catalog announcement:

(1) haven't there always been plugins?

yes. the catalog is a directory on top of the same plugin system: a reviewed list you can install from by name, `hermes plugins install <name>`, or from the Plugins page under Capabilities in Hermes Desktop.

(2) how are the community plugins vetted?

every entry gets in through a pull request that a maintainer reviews and merges, pinned to one exact commit. the entry also declares the tools, hooks and environment variables the plugin uses.

(3) what about updates after the first review?

the pin is the update path. when the author pushes new code, your install does not change until a new pin goes through the same review. a plugin pulled from the catalog goes on a removed list and the installer refuses it from then on.

(4) do I need to update Hermes to see new entries?

no. Hermes refreshes the catalog from the docs site at most every six hours, so new entries and removals arrive on their own.

(5) installed is not enabled

installing puts the plugin on disk. `hermes plugins enable <name>` switches it on, and `hermes plugins list` shows which ones came from the catalog.

(6) can I still install my own repos?

yes. `hermes plugins install <git url>` works for any repository, unreviewed and with a warning banner. the catalog is for finding plugins; the URL path is for your own.

(7) how do I get my plugin in?

one pull request that adds one yaml file to the plugin-catalog folder: you own the repo, it has a release, the validation check is green.

https://hermes-agent.nousresearch.com/docs/user-guide/features/plugin-catalog
