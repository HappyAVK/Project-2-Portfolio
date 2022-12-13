import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/drugs.jpg")

with col2:
    st.title("Alexander Southall")
    content= """I'm Alex, Im learning Python everyday, 
    I Graduated from the University of Greenwich with a specialization in animation, 
    but with python I aim to lean more into Software development, annd Data Science!"""
    st.info(content)

st.subheader("If any of these apps interest you, feel free to contact me about them!")