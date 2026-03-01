import streamlit as st
from utils.auth import login

st.set_page_config(page_title="KGL AI", layout="wide")

st.title("🚀 KGL AI Platform")

login()

st.write("Welcome to KGL AI Analytics System")
