import smtplib, ssl
import os
def send_mail(message):
    host = "smtp.mail.yahoo.com"
    port = 465
    username = "alexlsouthall@yahoo.com"
    password = os.getenv("PyPass")
    password1 = password
    receiver= "alexlsouthall@yahoo.com"
    contexti = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=contexti) as server:
        server.login(username, password1)
        server.sendmail(username, receiver, message)