# Day 9 - Extracting API data: pull name and email from the JSON response
import requests

url = 'https://randomuser.me/api/'
response = requests.get(url)

data = response.json()

name = data['results'][0]['name']['first']
email = data['results'][0]['email']

print('Name:', name)
print('Email:', email)

