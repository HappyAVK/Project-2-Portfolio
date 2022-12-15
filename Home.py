import streamlit as st
import pandas

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
df = pandas.read_csv("data.csv", sep=";")
col3, col4, col5= st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col5:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")