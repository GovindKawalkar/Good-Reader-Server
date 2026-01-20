import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Dashboard", layout="wide")

# ---- SESSION CHECK ----
if "logged_in" not in st.session_state:
    st.warning("Please login first")
    st.stop()

# ---- CSS ----
st.markdown("""
<style>
body {
    background-color: white;
}
.topbar {
    background: #ffffff;
    padding: 10px;
    border-bottom: 1px solid #ddd;
}
.card {
    background: #f9f9f9;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---- TOP BAR ----
st.markdown("<div class='topbar'>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    news_btn = st.button("📰 News & Articles")
with c2:
    blog_btn = st.button("✍️ Blogs")
with c3:
    book_btn = st.button("📚 Books")
st.markdown("</div>", unsafe_allow_html=True)

# ---- DATE FILTER ----
today = date.today()
yesterday = today - timedelta(days=1)
date_filter = st.radio("Select Date", ["Today", "Yesterday"])

selected_date = today if date_filter == "Today" else yesterday

# ================= NEWS & ARTICLES =================
if news_btn:
    st.header("📰 Newspaper & Articles")
    st.write(f"Showing for: **{selected_date}**")

    categories = {
        "Sports": "India won the series by 3-1.",
        "Education": "New education policy updates announced.",
        "Politics": "Parliament session highlights.",
        "Business": "Market shows strong growth today."
    }

    for k, v in categories.items():
        st.markdown(f"""
        <div class="card">
        <h4>{k}</h4>
        <p>{v}</p>
        <small>Date: {selected_date}</small>
        </div>
        """, unsafe_allow_html=True)

# ================= BLOG SECTION =================
if blog_btn:
    st.header("✍️ Blogs")

    blogs = [
        ("Future of AI", "AI will transform industries rapidly."),
        ("Education Growth", "Online education is booming."),
        ("Business Tips", "Smart investment strategies.")
    ]

    for title, desc in blogs:
        st.markdown(f"""
        <div class="card">
        <h4>{title}</h4>
        <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    st.button("Show More Blogs")

# ================= BOOK SECTION =================
if book_btn:
    st.header("📚 Books")

    col1, col2 = st.columns(2)

    # ---- FREE BOOKS ----
    with col1:
        st.subheader("📘 Free Books")
        st.markdown("""
        ⭐⭐⭐⭐☆ Python Basics  
        Learn Python from scratch.
        """)
        st.markdown("""
        ⭐⭐⭐☆☆ Data Science Intro  
        Beginner friendly guide.
        """)
        st.button("More Free Books")

    # ---- PREMIUM BOOKS ----
    with col2:
        st.subheader("💎 Premium Books")
        st.markdown("""
        ⭐⭐⭐⭐⭐ Advanced AI  
        Complete AI mastery guide.
        """)
        st.markdown("""
        ⭐⭐⭐⭐⭐ Business Strategy  
        High-level business planning.
        """)
        st.button("More Premium Books")

# ---- LOGOUT ----
st.sidebar.button("Logout", on_click=lambda: st.session_state.clear())
