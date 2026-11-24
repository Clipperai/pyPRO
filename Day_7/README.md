# Day 7 — Random Module & Guess the Number

**Focus:** the random module (randint) and a Guess-the-Number game in three levels.

## Files in this day

- **randomm.py** — generate a random number with randint
- **guess_the_num.py** — Guess the Number v1: one guess at a random number
- **guess_num_lev_2.py** — Guess the Number Level 2: keep guessing until correct
- **guess_num_lev_3.py** — Guess the Number Level 3: guessing loop with an attempts counter

## What I learned

- `random.randint(1, 10)` picks a random integer in a range
- A `while True` loop with `break` for "keep trying until correct"
- Counting attempts in a loop
- Handling wrong input with `try` / `except ValueError` so the game does not crash

## How to run

```
python randomm.py
python guess_num_lev_3.py
```

Part of my 30-day Python challenge (pyPRO).
