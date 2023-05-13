import requests
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\shahn\Python Code\Pycharm Env Vars\cheap-flight-tracker.env")

SHEETY_AUTH_TOKEN = os.environ["SHEETY_AUTH_TOKEN"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]


class DataManager:

    def __init__(self):
        self.authorization_headers = None
        self.data = None
        self.response = None
        self.update_data = None
        self.row_update_endpoint = None
        self.sheety_endpoint = SHEETY_ENDPOINT

    def get_dest_data(self):
        self.authorization_headers = {
            "Authorization": SHEETY_AUTH_TOKEN
        }
        self.response = requests.get(url=self.sheety_endpoint, headers=self.authorization_headers)
        try:
            self.data = self.response.json()['prices']
        except KeyError:
            print("Sorry, the sheety API is not available for the rest of the month. Please try again next month.")
            return None
        return self.data

    def update_rows(self):
        for row in self.data:
            self.row_update_endpoint = f"{self.sheety_endpoint}/{row['id']}"
            self.update_data = {
                "price": {
                    "city": row["city"],
                    "iataCode": row["iataCode"],
                    "lowestPrice": row["lowestPrice"],
                    "id": row["id"]
                }
            }
            self.response = requests.put(url=self.row_update_endpoint, json=self.update_data,
                                         headers=self.authorization_headers)
