import requests
import datetime as dt

USERNAME = "ikkraig"
TOKEN = "enter_valid_token"
CURRENT_DATE = dt.datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

# https://pixe.la/v1/users/ikkraig/graphs/graph.html
graph_params = {
    "id": "graph",
    "name": "Coding graph",
    "unit": "Hours",
    "type": "float",
    "color": "ichou",
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


def post_day(date, quantity="3"):
    value_endpoint = f"{graph_endpoint}/{graph_params['id']}"

    # TODO:
    # Insert data from pomodoro
    quantity = "5"

    value_params = {
        "date": date,
        "quantity": quantity
    }

    valid_response = False

    while not valid_response:
        response = requests.post(url=value_endpoint, json=value_params, headers=headers)
        print(response.text)
        data = response.json()
        valid_response = data["isSuccess"]


def update_day(day,quantity):
    update_params = {
        "quantity": quantity
    }
    update_endpoint = f"{graph_endpoint}/{graph_params['id']}/{day}"
    valid_response = False

    while not valid_response:
        response = requests.put(url=update_endpoint, json=update_params, headers=headers)
        print(response.text)
        data = response.json()
        valid_response = data["isSuccess"]


def delete_day(day):
    delete_endpoint = f"{graph_endpoint}/{graph_params['id']}/{day}"
    valid_response = False

    while not valid_response:
        response = requests.delete(url=delete_endpoint, headers=headers)
        print(response.text)
        data = response.json()
        valid_response = data["isSuccess"]


def get_quantity() -> int:
    pass

# post_day(CURRENT_DATE, get_quantity())

# EXTRA FUNCTIONALITY

# date_to_update = "20221102"
# quantity = "5"

# post_day(date_to_update, quantity)
# update_day(date_to_update, "3")
# delete_day(date_to_update)