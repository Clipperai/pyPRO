# Day 8 — Web Scraping & Quotes

**Focus:** requests + BeautifulSoup — fetching a page, parsing HTML, extracting quotes to a file.

## Files in this day

- **web_fetch.py** — fetch a web page with requests and print its HTML
- **parse_html.py** — fetch a page and print its title with BeautifulSoup
- **Quotes.py** — scrape quotes and save them to quotes.txt, one per line
- **Extract_quotes.py** — Quotes Generator: the scraper as a Streamlit web app
- **div.html** — a tiny practice HTML page
- **quotes.txt** — the quotes saved by Quotes.py

## What I learned

- `requests.get()` fetches a web page
- BeautifulSoup parses HTML so I can search it — `find_all()` by tag and class
- Extracted text can be written to a file, one item per line
- BeautifulSoup (`bs4`) is an external library, not part of the standard library

## How to run

```
python parse_html.py
python Quotes.py
streamlit run Extract_quotes.py
```

Part of my 30-day Python challenge (pyPRO).
