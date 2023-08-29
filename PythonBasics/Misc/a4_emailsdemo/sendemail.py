import smtplib
import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SENDER_EMAIL_ID = os.environ.get("SENDER_EMAIL_ID")
SENDER_EMAIL_PASSWORD = os.environ.get("SENDER_EMAIL_PASSWORD")

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

smtpObj.login(SENDER_EMAIL_ID, SENDER_EMAIL_PASSWORD)

receivers_mail = ['nikhil777grover@gmail.com',
                  'sauravgarg001@gmail.com', 'ansarh6074@gmail.com']
to_email_ids = ", ".join(receivers_mail)

results = smtpObj.sendmail(SENDER_EMAIL_ID, to_email_ids,
                           'Subject: Email from Python.\nAjay, Our Python Program is ready. We are all set for Demo. Sincerely, Swamy')

print(results)

smtpObj.quit()
