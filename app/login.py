import streamlit as st

st.title("Login Demo")

username = st.text_input("Username:")
password = st.text_input("Password:", type = "password")

#Login button
if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("You are in!")
    else:
        st.error("Please check you credential again! There is a mistake")        