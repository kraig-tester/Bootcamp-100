import smtplib
import datetime as dt

# MAILRU = "smtp.mail.ru"
# GMAIL = "smtp.gmail.com"
# sender_mail = "laonelove@mail.ru"
# reciever_mail = "ikrasnyanskiy123@gmail.com"

# with smtplib.SMTP(MAILRU) as connection:
#     connection.starttls()
#     connection.login(user=sender_mail, password='!Z!&cY001Hjv9u%EU')
#     connection.sendmail(from_addr=sender_mail, to_addrs=reciever_mail, msg="Hello")

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()

print(year, month, day_of_the_week)

date_of_birth = dt.datetime(year=1995, month=4, day=23)