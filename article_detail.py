import streamlit as st

art = st.session_state.article_data

st.image(art[1], use_container_width=True)
st.title(art[0])

st.write("""
Full article content goes here.
This page behaves like a real news website.
""")

st.caption("Admin: Govind | GoodReader")

if st.button("⬅ Back"):
    st.session_state.page = "dashboard"
    st.rerun()
