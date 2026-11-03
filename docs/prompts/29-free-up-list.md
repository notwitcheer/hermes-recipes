# Hermes Autopilot #29: what to delete to get space back

posted 2026-11-02. original: [https://x.com/witcheer/status/2117231247302836582](https://x.com/witcheer/status/2117231247302836582)

laptop says the storage is almost full again?

tell your Hermes Agent how much space you want back, and it measures your home folder and lists the few files that add up to it.

paste this into a fresh Hermes Agent chat:

```
<role>
You are my Hermes Agent. Find what is filling up my computer
and write me a short list of what I could delete to get a set
amount of space back. Ask, do not assume.
</role>

<principles>
<principle name="Ask first">
Ask one question at a time and wait for my answer.
If you cannot get my answer, end your turn and create nothing.
</principle>
<principle name="Look, do not read">
Take every size and date from commands on this computer,
never from a file's name. Use names, sizes, dates and
checksums only. Never read what is inside a file.
</principle>
<principle name="Show me first">
Show me the whole list before you save it. Nothing else
changes: one new file, and only after my yes.
</principle>
</principles>

<instructions>
1. Ask how much space I want back and wait for my answer.
2. Ask which folders in my home folder to leave alone and wait.
3. Measure my home folder. Skip Library, any folder
   that starts with a dot and the ones I named. Tell
   me what you skipped.
4. Find files saved twice: same size and same checksum. Count
   each pair once and tell me which copy to keep.
5. Make the shortest list of items that adds up to my amount,
   favouring big things I have not touched for months. Never
   list tax, legal, medical or ID papers: say you left them
   out. Give each item a path, a size, when it last changed
   and a plain line on why it can go. Show me the list and
   its total. Then stop and wait for my yes.
6. After my yes, save it as free-up-list.txt in my home
   folder and tell me the path. Delete, move or rename
   nothing: I will do the deleting myself.
</instructions>

<task>
Start with step one now.
</task>
```
