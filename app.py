import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GoodReader | Login",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "login"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- BACKGROUND ----------------
BACKGROUND_IMAGE = "https://images.unsplash.com/photo-1512820790803-83ca734da794"

st.markdown(f"""
<style>
html, body, .stApp {{
    height: 100%;
}}

.stApp {{
    background: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),
                url("{BACKGROUND_IMAGE}");
    background-size: cover;
    background-position: center;
}}

.login-box {{
    width: 240px;
    background: white;
    position: fixed;
    top: 20px;
    right: 20px;
    border-radius: 12px;
    padding: 14px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.4);
}}

.title {{
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    background: linear-gradient(90deg,
        red, orange, yellow, green, cyan, blue, violet);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN PAGE ----------------
if st.session_state.page == "login":

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:30px;">📘</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">Good Reader</div>', unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="Username", label_visibility="collapsed")
    password = st.text_input("Password", type="password", placeholder="Password", label_visibility="collapsed")

    if st.button("Login", use_container_width=True):
        if username == "Admin" and password == "admin123":
            with st.spinner("Loading dashboard..."):
                time.sleep(0.4)  # UX smoothness
                st.session_state.logged_in = True
                st.session_state.page = "dashboard"
                st.rerun()
        else:
            st.error("Invalid credentials")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.button("Sign up")
    with col2:
        st.button("New Account")

    st.markdown(
        '<p style="text-align:center;font-size:10px;color:gray;">Created by Govind</p>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- DASHBOARD ROUTE ----------------
elif st.session_state.page == "dashboard":
    import dashboard
