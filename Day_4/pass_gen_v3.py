import random
import string
import streamlit as st # type: ignore
import time

st.title("Password Generator")

length = int(st.number_input("Enter password length: "))

chars = string.ascii_letters + string.digits + string.punctuation

password = "" 

for i in range(length):
    password += random.choice(chars) 

if st.button("Generate Password:"):
    time.sleep(1)
    st.success(f"Strong Password: {password}")
