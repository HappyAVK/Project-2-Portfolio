import streamlit as st
from Grab_Google_Sheet import get_df
st.set_page_config(layout="wide")
col0, col1, col2 = st.columns(3)


with col1:
    st.title("Alexander Southall")

    st.image("images/thumbnail.png", width=300)

    boxes = st.selectbox(label="Page Selection", options=["About", "Programming Projects", "Contact via Email"])



match boxes:

    case "Contact via Email":
        from send_email import send_mail

        st.header("Contact here")

        st.subheader("Enter Your Email")

        with st.form(key="e_form"):
            user_email = st.text_input("Enter your Email")
            raw_message = st.text_area("Your Message")
            message = f"""\
        Subject: New email from: {user_email}

        From: {user_email} 
        {raw_message}
        """

            button = st.form_submit_button("Send")
            if button:
                send_mail(message)
                st.info("Message sent")
    case "Programming Projects":

        st.subheader("If any of these apps interest you, feel free to contact me about them!")
        df = get_df()
        col3, col4, col5 = st.columns([1.5, 0.5, 1.5])
        available_projects = df.loc[df["State"]=="Yes"]
        index = int(len(available_projects)/2)

        with col3:
            for index, row in available_projects[:index].iterrows():

                st.header(row["title"])
                st.write(row["description"])
                st.image("images/" + row["image"], width=200)
                st.write(f"[Github Repo]({row['url']})")

        with col5:
            for index, row in available_projects[index+1:].iterrows():

                st.header(row["title"])
                st.write(row["description"])
                st.image("images/" + row["image"], width=200)
                st.write(f"[Github Repo]({row['url']})")
    case "About":
        col4, col5, col6 = st.columns(3)
        with col5:
            st.write("Hi Im Alexander Southall I am a 2021 Graduate from the University of Greenwich in Games Design & Development, here you will find some Python projects I've implemented to develop my skills, please take a look and I would love to hear some feedback, thanks!")


