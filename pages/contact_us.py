import streamlit as st

st.header("Contact here")

st.subheader("Enter Your Email")

with st.form(key="e_form"):
    user_email=st.text_input("Enter your Email")
    message= st.text_area("Your Message")
    button = st.form_submit_button("Send")
    if button:
        print("HNNNNGGG SENT")