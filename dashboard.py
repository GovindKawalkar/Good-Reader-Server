import streamlit as st

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()


# ---------- FORCE WHITE BACKGROUND ----------
st.markdown("""
<style>
html, body, .stApp, .main, .block-container {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* Remove top padding */
.block-container {
    padding-top: 0rem !important;
}

/* Top bar */
.topbar {
    background-color: #ffffff;
    border-bottom: 1px solid #ddd;
    padding: 14px 40px;
    display: flex;
    align-items: center;
}

.site-name {
    font-size: 26px;
    font-weight: 800;
    color: #382110;
    margin-left: 10px;
}

.menu {
    margin-left: auto;
}

.menu span {
    margin-left: 24px;
    font-weight: 500;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# ---------- TOP BAR ----------
st.markdown("""
<div class="topbar">
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Book_icon_2.svg" height="32">
    <div class="site-name">GoodReader</div>
    <div class="menu">
        <span>Blog</span>
        <span>Free Books</span>
        <span>Premium Books</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")  # spacing

# ---------- CONTENT ----------
st.header("📚 Popular Books")

@st.cache_data(show_spinner=False)
def load_books():
    return [
        ("Atomic Habits", "https://m.media-amazon.com/images/I/91bYsX41DVL.jpg"),
        ("The Alchemist", "https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg"),
        ("Deep Work", "https://m.media-amazon.com/images/I/71g2ednj0JL.jpg"),
        ("Ikigai", "https://m.media-amazon.com/images/I/71tbalAHYCL.jpg"),
        ("Rich Dad Poor Dad", "https://m.media-amazon.com/images/I/81bsw6fnUiL.jpg"),
    ]
books = load_books()

with st.spinner("Preparing your reading space..."):
    st.sleep(0.5)


for i, book in enumerate(books):
    with cols[i]:
        st.image(book[1], use_container_width=True)
        st.markdown(f"**{book[0]}**")
