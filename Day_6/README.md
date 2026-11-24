# Day 6 — File Handling & Notes Saver

**Focus:** file handling — read/write/append, open()/close() vs with — and a Notes Saver in two levels.

## Files in this day

- **write_file.py** — open a file in write mode and write text
- **read_file.py** — open a file in read mode and print the contents
- **append_file.py** — open a file in append mode and add a line
- **bonus_file.py** — appending with the `with` statement
- **Notes.Saver.py** — Notes Saver v1: take a note and append it to notes.txt
- **Notes_saver_lev_2.py** — Notes Saver Level 2: menu version — add, view and exit
- **notes.txt** — the notes file these programs read and write

## What I learned

- File modes: `w` writes (overwrites), `r` reads, `a` appends
- Always close a file after using it — or use `with`, which closes it automatically
- A menu loop can turn basic file operations into a small useful app

## How to run

```
python write_file.py
python read_file.py
python Notes_saver_lev_2.py
```

Part of my 30-day Python challenge (pyPRO).
