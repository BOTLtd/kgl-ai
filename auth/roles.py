import streamlit as st

def require_role(role):
    user = st.session_state.get("user")

    if not user:
        st.warning("Login required")
        st.stop()

    # Example: check metadata
    if user.user_metadata.get("role") != role:
        st.error("Unauthorized")
        st.stop()
