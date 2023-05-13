import time
import requests
import smtplib
import os
from datetime import datetime

MY_LAT = -58.3294
MY_LONG = -29.4239925

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour

max_latitude = MY_LAT + 5
min_latitude = MY_LAT - 5

max_longitude = MY_LONG + 5
min_longitude = MY_LONG - 5

if sunset < current_hour < sunrise:
    is_dark = True
else:
    is_dark = False

if is_dark and max_latitude > iss_latitude > min_latitude and max_longitude > iss_longitude > \
        min_longitude:
    can_see = True
else:
    can_see = False

email = os.environ["EMAIL"]
password = os.environ["EMAIL_APP_PASSWORD"]

while True:
    time.sleep(60)
    if can_see:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email,
                                msg="Subject:Look Up!\n\nLook up! The ISS is above you!")
