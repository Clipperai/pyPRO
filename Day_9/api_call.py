import requests

url = 'https://randomuser.me/api/'
response = requests.get(url)

data = response.json()

print(data)

