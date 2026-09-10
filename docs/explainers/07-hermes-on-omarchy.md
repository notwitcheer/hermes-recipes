# release explainer #7: Hermes on Omarchy

posted 2026-09-09. original: [https://x.com/witcheer/status/2097677043412369747](https://x.com/witcheer/status/2097677043412369747)

Hermes Agent is built into Omarchy now. it is an Arch-based Linux setup where everything runs from the keyboard and one menu. 

here is what you get:

(1) the desktop app, from the menu

Omarchy menu > Install > AI > Hermes Desktop. it installs like any other Omarchy app and sets up the Hermes runtime on first launch.

(2) Hermes as your default agent

Setup > Defaults > Agent > Hermes. the agent entry in the menu now opens Hermes. the terminal, the default agent and the app all use the same installation.

(3) two skills come with the OS

Omarchy ships an `omarchy` skill and links it into Hermes for you. ask Hermes to change a keybinding, rearrange the bar, set up a hook that runs on theme change or build a theme from scratch, and it knows where the files live and what it must never touch.

(4) a crash becomes a question you can ask

when a program crashes, Omarchy shows a notification: click to diagnose with AI. that hands the crash to Hermes with a second built-in skill that reads the core dump and the system journal around that moment, rules out the boring causes first, and tells you whether it is worth reporting.

(5) your theme, everywhere

switch an Omarchy theme and Hermes follows: the desktop app, the TUI and the CLI take the same colours.
