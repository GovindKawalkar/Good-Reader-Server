import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Dashboard | Book Server",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f4f1ea;
}
.navbar {
    background: #f4f1ea;
    padding: 10px 30px;
    border-bottom: 1px solid #ddd;
}
.logo {
    font-size: 28px;
    font-weight: bold;
    color: #382110;
}
.book-card {
    background: white;
    padding: 15px;
    border-radius: 6px;
    margin-bottom: 15px;
    border: 1px solid #ddd;
}
.book-title {
    font-weight: bold;
    font-size: 16px;
}
.author {
    color: gray;
    font-size: 13px;
}
.read-btn {
    background: #409D69;
    color: white;
    padding: 6px 12px;
    border-radius: 4px;
    display: inline-block;
    margin-top: 10px;
}
.sidebar-box {
    background: white;
    padding: 12px;
    border-radius: 6px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TOP NAVBAR ----------------
st.markdown("""
<div class="navbar">
    <span class="logo">goodreads</span>
</div>
""", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
left, center, right = st.columns([1.2, 2.5, 1.2])

# ---------------- LEFT SIDEBAR ----------------
with left:
    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.subheader("👤 Your Profile")
    st.write("Govind Kawalkar")
    st.write("Books Read: 12")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.subheader("📘 Reading Challenge")
    st.progress(0.6)
    st.write("12 / 20 Books")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.subheader("📚 Want to Read")
    st.write("- Atomic Habits")
    st.write("- Deep Work")
    st.write("- Rich Dad Poor Dad")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CENTER FEED ----------------
with center:
    st.markdown('<div class="book-card">', unsafe_allow_html=True)
    st.markdown('<div class="book-title">A Court of Thorns and Roses</div>', unsafe_allow_html=True)
    st.markdown('<div class="author">by Sarah J. Maas</div>', unsafe_allow_html=True)
    st.write("⭐ ⭐ ⭐ ⭐ ☆")
    st.markdown('<div class="read-btn">Want to Read</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="book-card">', unsafe_allow_html=True)
    st.markdown('<div class="book-title">Throne of Glass</div>', unsafe_allow_html=True)
    st.markdown('<div class="author">by Sarah J. Maas</div>', unsafe_allow_html=True)
    st.write("⭐ ⭐ ⭐ ⭐ ⭐")
    st.markdown('<div class="read-btn">Currently Reading</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="book-card">', unsafe_allow_html=True)
    st.markdown('<div class="book-title">The Alchemist</div>', unsafe_allow_html=True)
    st.markdown('<div class="author">by Paulo Coelho</div>', unsafe_allow_html=True)
    st.write("⭐ ⭐ ⭐ ⭐ ☆")
    st.markdown('<div class="read-btn">Read</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RIGHT SIDEBAR ----------------
with right:
    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.subheader("📖 Recommendations")
    st.write("• It Ends With Us")
    st.write("• The Midnight Library")
    st.write("• Verity")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.subheader("🔥 Popular Now")
    st.write("• Harry Potter")
    st.write("• Percy Jackson")
    st.write("• Power of Habit")
    st.markdown('</div>', unsafe_allow_html=True)
