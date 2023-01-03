from email.message import EmailMessage
from dotenv import load_dotenv
import os
import ssl
import smtplib

load_dotenv()

email_sender = 'evgeny.ft@gmail.com'
password = os.environ.get("gmail_pass")

email_reciever = 'ekolodenets@yahoo.com'
subject = 'Just checking the mail'
body = '''
This is a body mail
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
