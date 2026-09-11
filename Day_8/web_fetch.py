import requests

url = 'https://quotes.toscrape.com'

response = requests.get(url)

print(response.text)

# api_key = "1bb2c1581ffa4e8e9f884846260103"
