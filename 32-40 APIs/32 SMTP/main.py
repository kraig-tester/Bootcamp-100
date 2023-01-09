# Given code is non-functional due to recent restrictions applied by mail services
import datetime as dt
import pandas as pd
import smtplib
import random

BIRTHDAY_FILE = "birthdays.csv"
EMAIL = "test@gmail.com"
PASSWORD = "password"

now = dt.datetime.now()
today = (now.month, now.day)

dates_csv = pd.read_csv(BIRTHDAY_FILE)
dates_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in dates_csv.iterrows()}

if today in dates_dict:
    b_day_person = dates_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", b_day_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=b_day_person["email"], 
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )



