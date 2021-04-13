import smtplib, sys, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("Mail Client v1.0 (Powered by Google SMTP)")
print("Copyright (c) 2020 miniprime1. All rights reserved.")
print("[Warning: Use google account only]\n")

email = input("Enter Your Email Address: ")
password = input("Enter Your Email Password: ")

msg = MIMEMultipart()
msg['From'] = email
recipient = input("Enter Recipient Email: ")
msg['To'] = recipient
msg['Subject'] = input("Enter Email Subject: ")

f = open('email.txt', 'w')
print("\nWrite body (To exit and send email, type \"SEND\")")
while True:
    before_data = input()
    if before_data == 'SEND': break
    data = before_data + "\n"
    f.write(data)
f.close
print("")

with open('email.txt', "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    try:
        server.login(email, password)
        server.sendmail(email, recipient, msg.as_string())
    except:
        print("\nError:")
        print("Allow it to run less secure app in \n“https://www.google.com/settings/security/lesssecureapps”, and try this again")
        input("\nPress enter key to exit")
        sys.exit()

print("Email sent success!")
os.remove("email.txt")
input("\nPress enter key to exit")