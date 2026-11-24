# Day 8 - Web fetching: fetch a web page with requests and print its HTML
import requests

url = 'https://quotes.toscrape.com'

response = requests.get(url)

print(response.text)
