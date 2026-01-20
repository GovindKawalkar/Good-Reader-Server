import streamlit as st
import time

st.set_page_config(page_title="Login", layout="centered")

# ---- CSS ----
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}
.login-box {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px #ccc;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='login-box'>", unsafe_allow_html=True)
st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if email == "Kawalkar123@gmail.com" and password == "GoviGod12":
        st.success("Login successful")
        st.session_state.logged_in = True
        time.sleep(0.3)  # very fast
        st.switch_page("dashboard.py")
    else:
        st.error("Invalid email or password")

st.markdown("</div>", unsafe_allow_html=True)
