import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GoodReader | Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- WHITE THEME CSS ----------------
st.markdown("""
<style>
/* GLOBAL WHITE BACKGROUND */
.stApp {
    background-color: #ffffff;
    color: #111;
    font-family: "Segoe UI", sans-serif;
}

/* REMOVE STREAMLIT DEFAULT PADDING */
.block-container {
    padding-top: 0rem;
}

/* TOP BAR */
.topbar {
    background: #ffffff;
    border-bottom: 1px solid #ddd;
    padding: 14px 40px;
    display: flex;
    align-items: center;
}
.topbar img {
    height: 36px;
    margin-right: 12px;
}
.site-name {
    font-size: 26px;
    font-weight: 800;
    color: #382110;
}
.menu {
    margin-left: auto;
}
.menu span {
    margin-left: 24px;
    font-weight: 500;
    cursor: pointer;
    color: #333;
}

/* SECTION TITLE */
.section-title {
    font-size: 22px;
    font-weight: 700;
    margin: 25px 0 10px;
}

/* CARD */
.card {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    padding: 10px;
}

/* BOOK IMAGE */
.book-img {
    border-radius: 4px;
}

/* BUTTON */
.read-btn {
    background: #409D69;
    color: white;
    padding: 6px 10px;
    border-radius: 4px;
    font-size: 13px;
    margin-top: 8px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TOP BAR ----------------
st.markdown("""
<div class="topbar">
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Book_icon_2.svg">
    <span class="site-name">GoodReader</span>
    <div class="menu">
        <span>Blog</span>
        <span>Free Books</span>
        <span>Premium Books</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- BOOK SECTION ----------------
st.markdown('<div class="section-title">📚 Popular Books</div>', unsafe_allow_html=True)

books = [
    ("Atomic Habits", "https://m.media-amazon.com/images/I/91bYsX41DVL.jpg"),
    ("The Alchemist", "https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg"),
    ("Deep Work", "https://m.media-amazon.com/images/I/71g2ednj0JL.jpg"),
    ("Rich Dad Poor Dad", "https://m.media-amazon.com/images/I/81bsw6fnUiL.jpg"),
    ("Ikigai", "https://m.media-amazon.com/images/I/71tbalAHYCL.jpg"),
]

cols = st.columns(5)
for i, book in enumerate(books):
    with cols[i]:
        st.image(book[1], use_container_width=True)
        st.markdown(f"**{book[0]}**")
        st.markdown('<div class="read-btn">Read More</div>', unsafe_allow_html=True)

# ---------------- NEWS SECTION ----------------
st.markdown('<div class="section-title">📰 News & Articles</div>', unsafe_allow_html=True)

news = [
    ("AI Changing Reading Habits", "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f"),
    ("Top 10 Books of 2026", "https://images.unsplash.com/photo-1507842217343-583bb7270b66"),
    ("Why Reading Is Important", "https://images.unsplash.com/photo-1509021436665-8f07dbf5bf1d"),
    ("Digital Libraries Growth", "https://images.unsplash.com/photo-1528207776546-365bb710ee93"),
    ("Future of Online Reading", "https://images.unsplash.com/photo-1519681393784-d120267933ba"),
]

cols = st.columns(5)
for i, art in enumerate(news):
    with cols[i]:
        st.image(art[1], use_container_width=True)
        st.markdown(f"**{art[0]}**")
        st.caption("By GoodReader Admin")
