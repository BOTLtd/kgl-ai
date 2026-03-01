import streamlit as st
from auth.roles import require_role

require_role("admin")

st.title("🔐 Admin Panel")
st.write("Only admins can see this")
