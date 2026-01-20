import streamlit as st

# ---------- TOP BAR ----------
st.markdown("""
<style>
.topbar {
    background: #382110;
    padding: 15px 40px;
    display: flex;
    align-items: center;
}
.topbar img {
    height: 40px;
    margin-right: 15px;
}
.topbar span {
    color: white;
    font-size: 26px;
    font-weight: bold;
}
.menu {
    margin-left: auto;
}
.menu span {
    color: white;
    margin-left: 20px;
    cursor: pointer;
    font-weight: 500;
}
.card {
    background: white;
    padding: 10px;
    border-radius: 6px;
    border: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Book_icon_2.svg">
    <span>GoodReader</span>
    <div class="menu">
        <span>Blog</span>
        <span>Free Books</span>
        <span>Premium Books</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------- BOOK SECTION ----------
st.subheader("📚 Popular Books")

books = [
    ("Atomic Habits", "James Clear",
     "https://m.media-amazon.com/images/I/91bYsX41DVL.jpg"),
    ("The Alchemist", "Paulo Coelho",
     "https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg"),
]

cols = st.columns(5)
for i, book in enumerate(books):
    with cols[i]:
        st.image(book[2], use_container_width=True)
        st.markdown(f"**{book[0]}**")
        st.caption(book[1])
        if st.button("Read More", key=book[0]):
            st.session_state.page = "book"
            st.session_state.book_data = book
            st.rerun()

# ---------- NEWS SECTION ----------
st.subheader("📰 News & Articles")

articles = [
    ("AI Changing Reading Habits",
     "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f"),
    ("Top 10 Books of 2026",
     "https://images.unsplash.com/photo-1507842217343-583bb7270b66"),
]

cols = st.columns(5)
for i, art in enumerate(articles):
    with cols[i]:
        st.image(art[1], use_container_width=True)
        st.markdown(f"**{art[0]}**")
        if st.button("Open", key=art[0]):
            st.session_state.page = "article"
            st.session_state.article_data = art
            st.rerun()
