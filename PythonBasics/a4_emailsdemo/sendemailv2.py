import smtplib
import os
import yfinance as yf

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

toaddr = 'nikhil777grover@gmail.com'
cc_receivers = ['sauravgarg001@gmail.com', 'ansarh6074@gmail.com']
cc_email_ids = ", ".join(cc_receivers)

#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
print(tickerData)

message_subject = "AIS - Python Email"
message_text = "Looks like we are learning more. Stock Price of MSFT: " + str(tickerData.info['currentPrice'])

message = "From: %s\r\n" % SENDER_EMAIL_ID + "To: %s\r\n" % toaddr + \
    "CC: %s\r\n" % cc_email_ids + \
    "Subject: %s\r\n" % message_subject + "\r\n" + message_text
toaddrs = [toaddr] + cc_receivers

results = smtpObj.sendmail(SENDER_EMAIL_ID, toaddrs, message)

print(results)

smtpObj.quit()
