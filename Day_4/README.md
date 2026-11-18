# Day 4 — Strings & Password Generator

**Focus:** strings — and a Password Generator built in three versions.

## Files in this day

- **my_string.py** — creating a string and checking its type
- **str_op.py** — string operations: joining two strings, `len()`, `lower()`, `upper()`
- **str_loop.py** — looping through a string letter by letter
- **pass_gen.py** — Password Generator v1: a random 8-character password (letters + digits)
- **pass_gen_v2.py** — Password Generator v2: choose the length, symbols included
- **pass_gen_v3.py** — Password Generator v3: the generator as a Streamlit web app

## What I learned

- Strings are sequences — you can loop over them letter by letter
- Useful string methods: `lower()`, `upper()`, and `len()` for length
- The `string` module gives ready-made character sets (`ascii_letters`, `digits`, `punctuation`)
- `random.choice()` picks one random character at a time

## How to run

```
python str_op.py
python pass_gen_v2.py
streamlit run pass_gen_v3.py
```

Part of my 30-day Python challenge (pyPRO).
