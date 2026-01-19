import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GoodReader Login",
    layout="wide",
)

# ---------------- OWNER SETTINGS ----------------
BACKGROUND_IMAGE_URL = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f"
LOGO_PATH = None  # Example: "logo.png"

ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "admin123"

# ---------------- CSS ----------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),
                    url("{BACKGROUND_IMAGE_URL}");
        background-size: cover;
        background-position: center;
    }}

    .login-box {{
        background-color: white;
        width: 260px;
        height: 300px;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.35);
        position: fixed;
        top: 18px;
        right: 18px;
    }}

    .title {{
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        background: linear-gradient(90deg,
            #ff3c3c,
            #ffb347,
            #ffee58,
            #4caf50,
            #00bcd4,
            #3f51b5,
            #9c27b0
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }}

    .footer {{
        text-align: center;
        font-size: 11px;
        color: #777;
        margin-top: 6px;
    }}

    .links {{
        text-align: center;
        font-size: 11px;
    }}

    .links a {{
        color: #1f77b4;
        text-decoration: none;
        margin: 0 3px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- LOGIN BOX ----------------
st.markdown('<div class="login-box">', unsafe_allow_html=True)

# Logo
if LOGO_PATH:
    st.image(LOGO_PATH, width=60)
else:
    st.markdown("<p style='text-align:center;font-size:32px;'>📖</p>", unsafe_allow_html=True)

# App Title
st.markdown('<div class="title">Good Reader</div>', unsafe_allow_html=True)

# Inputs
username = st.text_input("Username", key="username")
password = st.text_input("Password", type="password", key="password")

# Button
if st.button("Login", use_container_width=True):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        st.success("Login Successful")
        st.session_state["logged_in"] = True
        st.rerun()
    else:
        st.error("Invalid credentials")

# Links
st.markdown(
    """
    <div class="links">
        <a href="#">Sign up</a> |
        <a href="#">Forgot</a> |
        <a href="#">New</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown('<div class="footer">Created by Govind</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- REDIRECT ----------------
if st.session_state.get("logged_in"):
    st.switch_page("pages/dashboard.py")

