# Imports
import datetime as dt
import smtplib
import random
from pandas import *
import os

from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\shahn\Python Code\Pycharm Env Vars\email-stuff.env")

# Variables
birthdays = {}
letters = []
emails = {}

# Setting up smtplib
email = os.environ["EMAIL"]
password = os.environ["EMAIL_APP_PASSWORD"]


# Letters
def read_letters(name):
    global letters
    with open("letter_templates/letter_1.txt", mode="r") as file:
        letter_1 = file.readlines()
        letter_1 = "".join(letter_1)
        letter_1 = letter_1.replace("[NAME]", name)
        letters.append(letter_1)

    with open("letter_templates/letter_2.txt", mode="r") as file:
        letter_2 = file.readlines()
        letter_2 = "".join(letter_2)
        letter_2 = letter_2.replace("[NAME]", name)
        letters.append(letter_2)

    with open("letter_templates/letter_3.txt", mode="r") as file:
        letter_3 = file.readlines()
        letter_3 = "".join(letter_3)
        letter_3 = letter_3.replace("[NAME]", name)
        letters.append(letter_3)


# 1. Read birthdays.csv
birthdays_file = read_csv("birthdays.csv")
birthdays_dict = birthdays_file.to_dict(orient="index")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
date = now.date()
current_hour = now.hour
current_minute = now.minute

people_amount = len(birthdays_dict)
for num in range(0, people_amount):
    current_spot = birthdays_dict[int(num)]["name"]
    emails[birthdays_dict[int(num)]["name"]] = birthdays_dict[int(num)]["email"]
    birthdays[current_spot] = dt.datetime(year=now.year, month=birthdays_dict[num]["month"],
                                          day=birthdays_dict[num]["day"], hour=random.randint(9, 13),
                                          minute=random.randint(1, 59))

for person in birthdays.keys():
    if birthdays[person].date() == date:  # and birthdays[person].hour == current_hour and birthdays[person].minute == \
        # current_minute:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        read_letters(person)
        letter_to_send = random.choice(letters)
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=emails[person], msg=f"Subject:Happy Birthday!\n\n"
                                                                              f"{letter_to_send}")
