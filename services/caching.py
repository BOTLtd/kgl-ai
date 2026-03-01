import streamlit as st

@st.cache_data(ttl=60)
def cache_data(func, *args):
    return func(*args)
