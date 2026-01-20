import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GoodReader | Login",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- BACKGROUND ----------------
BACKGROUND_IMAGE = "https://images.unsplash.com/photo-1512820790803-83ca734da794"

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

# ---------------- LOGIN BOX ----------------
st.markdown('<div class="login-box">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center;font-size:30px;">📘</div>', unsafe_allow_html=True)
st.markdown('<div class="title">Good Reader</div>', unsafe_allow_html=True)

username = st.text_input("Username", placeholder="Username", label_visibility="collapsed")
password = st.text_input("Password", type="password", placeholder="Password", label_visibility="collapsed")

if st.button("Login", use_container_width=True):
    if username == "Admin" and password == "admin123":
        st.session_state.logged_in = True
        st.success("Login successful")
        st.page_link("pages/dashboard.py", label="Go to Dashboard ➜")
    else:
        st.error("Invalid credentials")

st.divider()

# ---------------- SAFE NAVIGATION ----------------
st.page_link("pages/signup.py", label="Sign up", icon="📝")
st.page_link("pages/signup.py", label="New Account", icon="➕")

st.markdown('<p style="text-align:center;font-size:10px;color:gray;">Created by Govind</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
