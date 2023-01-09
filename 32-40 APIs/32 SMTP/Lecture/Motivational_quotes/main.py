from calendar import week
import smtplib
import datetime as dt
import random

YAHOO_SMTP = "smtp.mail.yahoo.com"
YAHOO_EMAIL = "ikrasnyanskiy123@yahoo.com"
RECEIVER = "ikrasnyanskiy123@gmail.com"
PASSWORD = "tdN!RhU*2vF1kb%4"

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)

print(quote)
with smtplib.SMTP(YAHOO_SMTP) as connection:
    connection.starttls()
    connection.login(user=YAHOO_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=YAHOO_EMAIL, to_addrs=RECEIVER, 
        msg=f"Monday's quote,\n\n{quote}\n\nSent by quote bot."
    )