import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GoodReader",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION DEFAULTS ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_page" not in st.session_state:
    st.session_state.current_page = "login"

# ---------------- ROUTER ----------------
def router():
    if st.session_state.logged_in:
        st.page_link("pages/dashboard.py", label="Go to Dashboard", icon="📊")
    else:
        st.page_link("index.py", label="Login", icon="🔐")
        st.page_link("pages/signup.py", label="Sign up", icon="📝")

# ---------------- HEADER ----------------
st.markdown("""
<h2 style='text-align:center;'>📚 GoodReader Library Recommendation Server</h2>
""", unsafe_allow_html=True)

st.divider()

# ---------------- ROUTING MENU ----------------
router()

st.divider()

# ---------------- INFO ----------------
st.info(
    "Use the navigation above to Login, Sign up, or access Dashboard after authentication."
)
