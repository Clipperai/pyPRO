import requests
import streamlit as st # type: ignore
import time as t

api_key = "write_your_own_api_key"

st.set_page_config("Weather App")

city = st.text_input("Enter City Name: ")

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

response = requests.get(url)
data = response.json()

location = data['location']['name']
temperature = data['current']['temp_c']
condition = data['current']['condition']['text']
humidity = data['current']['humidity']

if st.button("Get Details"):

    with st.spinner("Loading..."):
        t.sleep(2)

        st.balloons()

        st.write("City:", location)
        st.write("Temperature:", temperature, "°C")
        st.write("Condition:", condition)
        st.write("Humidity:", humidity, "%")
