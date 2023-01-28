import smtplib, ssl
from streamlit import secrets
def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "asoutavk@gmail.com"
    password1 = secrets["key"]
    receiver= "alexlsouthall@yahoo.com"
    contexti = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=contexti) as server:
        server.login(username, password1)
        server.sendmail(username, receiver, message)