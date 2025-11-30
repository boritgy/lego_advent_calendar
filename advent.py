import streamlit as st
import json

st.title('Adventi naptár')

password = st.text_input("Jelszó:")

with open('days.json', 'r') as file:
    data = json.load(file)

filename = data.get(password)

if filename:
    st.pdf(f'files\\{filename}')