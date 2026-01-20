import streamlit as st

if not st.session_state.get("logged_in"):
    st.error("Please login first")
    st.stop()

st.title("📊 GoodReader Dashboard")
