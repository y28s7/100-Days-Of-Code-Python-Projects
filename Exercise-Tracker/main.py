import os
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\shahn\Python Code\Pycharm Env Vars\exercise-tracker.env")

now = datetime.now()

date = now.strftime("%m/%d/%Y")
time = now.strftime('%I:%M %p')

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

query = input("Input your exercises (in metric form): ")

exercise_data_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_data_json = {
    "query": query,
    "gender": os.environ["GENDER"],
    "weight_kg": os.environ["WEIGHT"],
    "height_cm": os.environ["HEIGHT"],
    "age": os.environ["AGE"]
}
response = requests.post(url=exercise_data_endpoint, headers=headers, json=exercise_data_json)
exercise_data = response.json()

sheet_endpoint = os.environ["SHEETY_ENDPOINT"]

sheet_headers = {
    "Authorization": os.environ["SHEETY_AUTH"]
}

for exercise in exercise_data["exercises"]:

    sheet_inputs = {
        "workout": {
            "date": str(date),
            "time": str(time),
            "exercise": str(exercise["name"]).title(),
            "duration": str(exercise['duration_min']),
            "calories": str(exercise['nf_calories'])
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs,headers=sheet_headers)

    print(sheet_response.text)
