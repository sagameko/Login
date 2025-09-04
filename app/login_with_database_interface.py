import streamlit as st
import sqlite3

#Check creadential

def check_user(username, password):
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result

st.title("Login with user Credential within database!")

username = st.text_input("Username:")
password = st.text_input("Password:", type = "password")

if st.button("Login") :
    user = check_user(username, password)
    if user:
        st.success("Login Successfully")
    else:
        st.error("Login failed!")