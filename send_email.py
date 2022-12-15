import smtplib, ssl


host = "smtp.mail.yahoo.com"
port = 465
username = "alexlsouthall@yahoo.com"
password = "jjzvtcbtjjxvqbix"
receiver= "allalexandersouth@gmail.com"
message = """\
Subject: Tesst
testest"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)