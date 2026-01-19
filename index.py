import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GoodReader - Login",
    layout="wide",
)

# ---------------- OWNER SETTINGS ----------------
BACKGROUND_IMAGE_URL = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f"
LOGO_PATH = None  # Example: "logo.png" (upload file & set path)

ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "admin123"

# ---------------- CSS STYLING ----------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(
            rgba(0,0,0,0.4),
            rgba(0,0,0,0.4)
        ),
        url("{BACKGROUND_IMAGE_URL}");
        background-size: cover;
        background-position: center;
    }}

    .login-box {{
        background-color: white;
        width: 330px;
        padding: 25px;
        border-radius: 14px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
        position: fixed;
        top: 20px;
        right: 20px;
    }}

    .app-title {{
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        background: linear-gradient(90deg,
            #ff0000,
            #ff7f00,
            #ffff00,
            #00ff00,
            #00ffff,
            #0000ff,
            #8b00ff
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 15px;
    }}

    .footer-text {{
        text-align: center;
        font-size: 12px;
        margin-top: 15px;
        color: gray;
    }}

    .link-text {{
        text-align: center;
        font-size: 13px;
    }}

    .link-text a {{
        text-decoration: none;
        color: #1f77b4;
        margin: 0 6px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- LOGIN BOX ----------------
st.markdown('<div class="login-box">', unsafe_allow_html=True)

# Logo
if LOGO_PATH:
    st.image(LOGO_PATH, width=80)
else:
    st.markdown("<p style='text-align:center;font-size:40px;'>📚</p>", unsafe_allow_html=True)

# App Name
st.markdown('<div class="app-title">Good Reader</div>', unsafe_allow_html=True)

# Login Inputs
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login Button
if st.button("Login", use_container_width=True):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        st.success("Login Successful ✅")
        st.session_state["logged_in"] = True
        st.session_state["user"] = "Admin"
        st.rerun()
    else:
        st.error("Invalid Username or Password ❌")

# Links
st.markdown(
    """
    <div class="link-text">
        <a href="#">Sign Up</a> |
        <a href="#">Forgot Password</a> |
        <a href="#">New Account</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown('<div class="footer-text">Created by Govind</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- AFTER LOGIN ----------------
if st.session_state.get("logged_in"):
    st.switch_page("pages/dashboard.py")
