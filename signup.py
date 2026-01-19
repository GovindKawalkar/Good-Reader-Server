import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GoodReader | Create Account",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #6a11cb, #2575fc);
}

.signup-box {
    background: white;
    max-width: 420px;
    margin: auto;
    margin-top: 60px;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.3);
}

.logo {
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 4px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    margin-bottom: 20px;
}

.small-text {
    font-size: 12px;
    color: gray;
}

.footer {
    text-align: center;
    font-size: 12px;
    color: white;
    margin-top: 25px;
}

.footer a {
    color: #ddd;
    text-decoration: none;
    margin: 0 6px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIGN UP BOX ----------------
st.markdown('<div class="signup-box">', unsafe_allow_html=True)

st.markdown('<div class="logo">GoodReader</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create Account</div>', unsafe_allow_html=True)

name = st.text_input("Your name", placeholder="First and last name")
email = st.text_input("Email")
password = st.text_input("Password", type="password", placeholder="At least 6 characters")
st.markdown('<div class="small-text">Passwords must be at least 6 characters.</div>', unsafe_allow_html=True)
confirm_password = st.text_input("Re-enter password", type="password")

if st.button("Create account", use_container_width=True):
    if not name or not email or not password or not confirm_password:
        st.error("All fields are required")
    elif len(password) < 6:
        st.error("Password must be at least 6 characters")
    elif password != confirm_password:
        st.error("Passwords do not match")
    else:
        st.success("Account created successfully 🎉")
        st.switch_page("index.py")

st.markdown("""
<p class="small-text">
By creating an account, you agree to the GoodReader
<b>Terms of Service</b> and <b>Privacy Policy</b>
</p>

<p class="small-text">
Already have an account?
<a href="#" onclick="window.location.href='/'">Sign in</a>
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <a href="#">Terms of Service</a>
    <a href="#">Privacy</a>
    <a href="#">Help</a><br>
    © 2026 Goodreads LLC
</div>
""", unsafe_allow_html=True)
