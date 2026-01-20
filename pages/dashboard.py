import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GoodReader | Dashboard",
    layout="wide"
)

# ---------------- FORCE CSS ----------------
st.markdown("""
<style>
/* GLOBAL */
html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
    background-color: #f4f1ea;
}

/* NAVBAR */
.navbar {
    background-color: #f4f1ea;
    padding: 15px 40px;
    border-bottom: 1px solid #ddd;
}
.logo {
    font-size: 30px;
    font-weight: 800;
    color: #382110;
}

/* CARDS */
.card {
    background: white;
    padding: 15px;
    border-radius: 6px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}

/* BOOK */
.book-title {
    font-size: 17px;
    font-weight: bold;
    color: #382110;
}
.author {
    font-size: 13px;
    color: #777;
}
.rating {
    color: #f4c150;
    font-size: 16px;
}
.btn {
    background: #409D69;
    color: white;
    padding: 6px 12px;
    border-radius: 4px;
    font-size: 13px;
    display: inline-block;
    margin-top: 8px;
}

/* SIDEBAR BOX */
.sidebar-box {
    background: white;
    padding: 12px;
    border-radius: 6px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
st.markdown("""
<div class="navbar">
    <span class="logo">goodreads</span>
</div>
""", unsafe_allow_html=True)

st.write("")  # spacing

# ---------------- LAYOUT ----------------
left, center, right = st.columns([1.3, 3, 1.3])

# ---------------- LEFT ----------------
with left:
    st.markdown("""
    <div class="sidebar-box">
        <h4>👤 Your Profile</h4>
        <p>Govind Kawalkar</p>
        <p>Books Read: 12</p>
    </div>

    <div class="sidebar-box">
        <h4>📘 Reading Challenge</h4>
        <p>12 / 20 Books</p>
    </div>

    <div class="sidebar-box">
        <h4>📚 Want to Read</h4>
        <p>Atomic Habits</p>
        <p>Deep Work</p>
        <p>Rich Dad Poor Dad</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CENTER FEED ----------------
with center:
    st.markdown("""
    <div class="card">
        <div class="book-title">A Court of Thorns and Roses</div>
        <div class="author">by Sarah J. Maas</div>
        <div class="rating">★★★★★</div>
        <div class="btn">Want to Read</div>
    </div>

    <div class="card">
        <div class="book-title">Throne of Glass</div>
        <div class="author">by Sarah J. Maas</div>
        <div class="rating">★★★★☆</div>
        <div class="btn">Currently Reading</div>
    </div>

    <div class="card">
        <div class="book-title">The Alchemist</div>
        <div class="author">by Paulo Coelho</div>
        <div class="rating">★★★★☆</div>
        <div class="btn">Read</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- RIGHT ----------------
with right:
    st.markdown("""
    <div class="sidebar-box">
        <h4>📖 Recommendations</h4>
        <p>It Ends With Us</p>
        <p>The Midnight Library</p>
        <p>Verity</p>
    </div>

    <div class="sidebar-box">
        <h4>🔥 Popular Now</h4>
        <p>Harry Potter</p>
        <p>Percy Jackson</p>
        <p>The Power of Habit</p>
    </div>
    """, unsafe_allow_html=True)
