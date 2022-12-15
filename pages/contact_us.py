import streamlit as st
from send_email import send_mail
st.header("Contact here")

st.subheader("Enter Your Email")

with st.form(key="e_form"):
    user_email=st.text_input("Enter your Email")
    raw_message= st.text_area("Your Message")
    message = f"""\
Subject: New email from: {user_email}

From: {user_email} 
{raw_message}
"""

    button = st.form_submit_button("Send")
    if button:
        send_mail(message)
        st.info("Message sent")