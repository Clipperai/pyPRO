# Day 9 — APIs & Weather App

**Focus:** APIs with requests — calling JSON APIs, extracting fields, and a Weather App in two levels.

## Files in this day

- **api_call.py** — fetch JSON data from an API with requests
- **extract_info.py** — pull name and email from the JSON response
- **Weather_app.py** — Weather App v1: current weather for a city using WeatherAPI
- **Weather_app_lev_2.py** — Weather App v2: the Weather App as a Streamlit web app

## What I learned

- An API returns JSON, which Python reads like a dictionary
- Extracting nested fields step by step — e.g. name and email from the results
- APIs can return an error instead of data — check for an `"error"` key before using the data
- API keys are secrets: use your own key (placeholder in the code), never share a real one

## How to run

```
python api_call.py
python Weather_app.py
streamlit run Weather_app_lev_2.py
```

Part of my 30-day Python challenge (pyPRO).
