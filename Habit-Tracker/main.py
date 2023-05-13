import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\shahn\Python Code\Pycharm Env Vars\habit-tracker.env")

now = datetime.now()
pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["USER_TOKEN"]
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Hours Coded Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date_to_put_pixel = now.strftime("%Y%m%d")

pixel_data = {
    "date": date_to_put_pixel,
    "quantity": input("Input how many hours you coded today: ")
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
while "Please retry this request" in response.text:
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print("Success")

pixel_update_endpoint = f"{pixel_creation_endpoint}/{date_to_put_pixel}"

pixel_update_data = {
    "quantity": "5"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# while "Please retry this request" in response.text:
#     response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print("Successful")

pixel_delete_endpoint = pixel_update_endpoint

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
