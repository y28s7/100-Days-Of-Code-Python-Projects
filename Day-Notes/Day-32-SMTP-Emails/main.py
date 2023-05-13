# import smtplib
#
# my_email = "subjecttest.1234.56"
# password = "kucsgtbwgafimqhj"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="subject.1234@yahoo.com", msg="Subject:hello\n\nHI")
#
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
# print(day_of_the_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=12)
# print(date_of_birth)

import datetime as dt
import smtplib
from random import choice

my_email = "subjecttest.1234.56"
password = "kucsgtbwgafimqhj"

with open("quotes.txt", mode="r") as file:
    quotes = file.readlines()

quote_to_send = choice(quotes)

now = dt.datetime.now()
day_week = now.weekday()
if day_week == day_week:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Motivational "
                                                                                   f"Quote\n\n{quote_to_send}")
