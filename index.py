import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GoodReader | Login",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SETTINGS ----------------
BACKGROUND_IMAGE = "https://images.unsplash.com/photo-1512820790803-83ca734da794"

ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "admin123"

# ---------------- CSS ----------------
st.markdown(f"""
<style>
.stApp {{
    background: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),
                url("{BACKGROUND_IMAGE}");
    background-size: cover;
    background-position: center;
}}

.login-box {{
    width: 240px;
    height: 260px;
    background: white;
    position: fixed;
    top: 20px;
    right: 20px;
    border-radius: 12px;
    padding: 14px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.4);
}}

.logo {{
    text-align: center;
    font-size: 30px;
}}

.title {{
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    background: linear-gradient(90deg,
        red, orange, yellow, green, cyan, blue, violet);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 6px;
}}

.footer {{
    text-align: center;
    font-size: 10px;
    color: gray;
    margin-top: 4px;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN BOX ----------------
st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="logo">📘</div>', unsafe_allow_html=True)
st.markdown('<div class="title">Good Reader</div>', unsafe_allow_html=True)

username = st.text_input("Username", placeholder="Username", label_visibility="collapsed")
password = st.text_input("Password", type="password", placeholder="Password", label_visibility="collapsed")

if st.button("Login", use_container_width=True):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        st.session_state["logged_in"] = True
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Invalid Username or Password")

# ---------------- NAV BUTTONS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Sign up"):
        st.switch_page("pages/signup.py")

with col2:
    st.button("Forgot")

with col3:
    st.button("New")

st.markdown('<div class="footer">Created by Govind</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
