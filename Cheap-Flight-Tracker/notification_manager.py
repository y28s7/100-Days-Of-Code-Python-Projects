from flight_data import FlightData
import smtplib
import os
import requests
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\shahn\Python Code\Pycharm Env Vars\email-stuff.env")

EMAIL = os.environ["EMAIL"]
EMAIL_APP_PASSWORD = os.environ["EMAIL_APP_PASSWORD"]


class NotificationManager:

    def __init__(self):
        self.email = EMAIL
        self.app_password = EMAIL_APP_PASSWORD
        self.endpoint = os.environ["SHEETY_USER_ENDPOINT"]
        self.headers = {
            "Authorization": os.environ["SHEETY_AUTH_TOKEN"]
        }

    def get_user_emails(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        user_data = response.json()["users"]
        user_emails = []
        for person in user_data:
            user_emails.append(person["email"])
        return user_emails

    def send_emails(self, flight_data: FlightData, city_sheet_data):
        user_emails = self.get_user_emails()
        for email in user_emails:
            google_flight_link = f"https://www.google.co.uk/travel/flights?lang=en#flt=STN." \
                                 f"{flight_data.to_airport}.{flight_data.out_date}*{flight_data.to_airport}" \
                                 f".STN.{flight_data.return_date}"
            try:
                if flight_data.price < city_sheet_data["lowestPrice"]:

                    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                        connection.starttls()
                        connection.login(user=email, password=self.app_password)

                        if flight_data.stopovers > 0:
                            message = f"Subject:Low Price Alert to fly to {flight_data.to_city}\n\nOnly " \
                                      f"{flight_data.price} " \
                                      f"pounds" \
                                      f" to fly from {flight_data.from_city}-{flight_data.from_airport} to " \
                                      f"{flight_data.to_city}-{flight_data.to_airport}!" \
                                      f" Depart on {flight_data.out_date[0]}" \
                                      f" and " \
                                      f"return on " \
                                      f"{flight_data.return_date[0]}.\n\nFlight has {flight_data.stopovers} stopovers," \
                                      f" first one being {flight_data.via_city}\n{google_flight_link}"
                        else:
                            message = f"Subject:Low Price Alert to fly to {flight_data.to_city}\n\n" \
                                      f"Only {flight_data.price} " \
                                      f"pounds" \
                                      f" to fly from {flight_data.from_city}-{flight_data.from_airport} to " \
                                      f"{flight_data.to_city}-{flight_data.to_airport}!" \
                                      f" Depart on {flight_data.out_date[0]}" \
                                      f" and " \
                                      f"return on " \
                                      f"{flight_data.return_date[0]}.\n{google_flight_link}"

                        connection.sendmail(from_addr=self.email, to_addrs=self.email, msg=message)
            except AttributeError:
                return
