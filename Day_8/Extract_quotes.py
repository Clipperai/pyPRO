from bs4 import BeautifulSoup
import requests
import streamlit as st # type: ignore
import time as t

st.set_page_config("Quotes Generator")

st.title("Welcome to Quotes Generator Tool")

url = "https://quotes.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all('span', class_='text')   

if st.button("Generate"):
    with st.spinner("Generating..."):
        t.sleep(2)
        
        for quote in quotes:
            st.write(quote.text)