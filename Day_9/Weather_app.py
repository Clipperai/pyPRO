# Day 9 - Weather App v1: current weather for a city using WeatherAPI
import requests

# Add your WeatherAPI key here
api_key = "YOUR_API_KEY"

city = 'london'

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

response = requests.get(url)
try:
    data = response.json()
except Exception:
    print("Error: Could not get weather data. Check your API key.")
    exit()

if "error" in data:
    print("Error:", data["error"]["message"])
    exit()

location = data["location"]["name"]
temperature = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]
humidity = data["current"]["humidity"]

print("City:", location)
print("Temperature:", temperature, "°C")
print("Condition:", condition)
print("Humidity:", humidity, "%")
