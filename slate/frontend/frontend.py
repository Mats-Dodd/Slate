import streamlit as st
import requests

API_ENDPOINT = "http://127.0.0.1:8000/"

st.title("Slate's Words for Tomorrow")

response = requests.get(API_ENDPOINT)
if response.status_code == 200:
    st.write(response.json()['message'])
else:
    st.write("Failed to connect to the backend API!")