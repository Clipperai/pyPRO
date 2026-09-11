from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text) # type: ignore
