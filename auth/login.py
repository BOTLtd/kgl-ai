import streamlit as st
from db.supabase_client import supabase

def login():
    st.sidebar.title("🔐 Login")

    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        res = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if res.user:
            st.session_state["user"] = res.user
            st.session_state["token"] = res.session.access_token
        else:
            st.error("Login failed")
