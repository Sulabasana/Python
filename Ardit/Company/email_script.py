import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username ="joachim.magath@gmail.com"
password = "npicgckrskrljmcq"

receiver = "joachim.magath@gmail.com"
my_context = ssl.create_default_context()
message = """\
Subject: Hi!
Hi!
How are you mordo?
mfg
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message )
