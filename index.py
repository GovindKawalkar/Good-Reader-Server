import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GoodReader Login",
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
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                url("{BACKGROUND_IMAGE}");
    background-size: cover;
    background-position: center;
}}

.logo {{
    text-align: center;
    font-size: 28px;
}}

.title {{
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    background: linear-gradient(90deg,
        red, orange, yellow, green, cyan, blue, violet);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
}}

.footer {{
    text-align: center;
    font-size: 10px;
    color: gray;
    margin-top: 4px;
}}

.links {{
    text-align: center;
    font-size: 10px;
}}

.links a {{
    text-decoration: none;
    color: #1f77b4;
    margin: 0 2px;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN BOX ----------------
st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="logo">📘</div>', unsafe_allow_html=True)
st.markdown('<div class="title">Good Reader</div>', unsafe_allow_html=True)

username = st.text_input("Username", label_visibility="collapsed", placeholder="Username")
password = st.text_input("Password", type="password", label_visibility="collapsed", placeholder="Password")

if st.button("Login", use_container_width=True):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        st.session_state.logged_in = True
        st.success("Login successful")
        st.rerun()
    else:
        st.error("Invalid credentials")

st.markdown(
st.markdown("**Already have an account?**")
if st.button("Sign up", key="signup_link"):
    st.switch_page("pages/signup.py")
    <a href="#">Forgot</a> |
    <a href="#">New</a>
</div>
, unsafe_allow_html=True)

st.markdown('<div class="footer">Created by Govind</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- REDIRECT ----------------
if st.session_state.get("logged_in"):
    st.switch_page("pages/dashboard.py")
