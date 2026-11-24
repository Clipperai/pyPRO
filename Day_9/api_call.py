# Day 9 - API call: fetch JSON data from an API with requests
import requests

url = 'https://randomuser.me/api/'
response = requests.get(url)

data = response.json()

print(data)

