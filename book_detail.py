import streamlit as st

book = st.session_state.book_data

st.image(book[2], width=300)
st.title(book[0])
st.subheader(book[1])

st.write("""
This is a full online reading section.
Here you can show:
• Book summary  
• Author info  
• Reading chapters  
• Premium access logic  
""")

st.caption("Admin: Govind | GoodReader")

if st.button("⬅ Back"):
    st.session_state.page = "dashboard"
    st.rerun()
