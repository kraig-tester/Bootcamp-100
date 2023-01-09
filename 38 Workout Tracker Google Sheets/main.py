import requests
import datetime as dt
from requests.auth import HTTPBasicAuth

NUTRONIX_ID = "enter_nutronix_id"
NUTRONIX_KEY = "enter_nutronix_token"
SHEETY_KEY = "Bearer your_bearer_key"
SHEETY_ROW_ENDPOINT = "https://api.sheety.co/enter_your_url"

nutronix_endpoint = "https://trackapi.nutritionix.com/v2/"
exercise_endpoint = nutronix_endpoint + "natural/exercise"


headers_nutronix = {
    "x-app-id": NUTRONIX_ID,
    "x-app-key": NUTRONIX_KEY,
    "Content-Type": "application/json"
}

user_query = input("What was your workout today?: ")

exercise_params = {
    "query": user_query,
    "gender":"male",
    "weight_kg": 105,
    "height_cm": 185,
    "age": 27
}

response = requests.post(url=exercise_endpoint, json=exercise_params,headers=headers_nutronix)
 
exercises = response.json()["exercises"]

current_date = dt.datetime.now()
date = current_date.strftime("%d/%m/%Y")
time = current_date.strftime("%H:%M:%S")

# Basic auth
# sheety_basic_auth = HTTPBasicAuth('your_username', 'your_password')

# Bearer auth
# can be used with basic as well
headers_sheety_bearer = {
    "Authorization": SHEETY_KEY
}

for item in exercises:
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": item["name"],
            "duration": item["duration_min"],
            "calories": item["nf_calories"]
        }
    }
    
    # Basic auth
    # response = requests.post(url=sheety_row_endpoint, json=sheety_params, auth=sheety_basic_auth)

    # Bearer auth
    response = requests.post(url=SHEETY_ROW_ENDPOINT, json=sheety_params, headers=headers_sheety_bearer)

    print(response.text)
 

