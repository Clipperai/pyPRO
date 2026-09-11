import requests

api_key = "78a555d22cc04b3d8ac140754260603"

city = 'london'

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

response = requests.get(url)
data = response.json()

location = data["location"]["name"]
temperature = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]
humidity = data["current"]["humidity"]

print("City:", location)
print("Temperature:", temperature, "°C")
print("Condition:", condition)
print("Humidity:", humidity, "%")