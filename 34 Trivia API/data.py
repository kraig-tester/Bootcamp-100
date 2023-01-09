import requests

TRIVIA_API = "https://opentdb.com/api.php"
PARAMS = {
    "amount": "10",
    "type": "boolean"
}

response = requests.get(url=TRIVIA_API, params=PARAMS)
response.raise_for_status()
data = response.json()

question_data = data["results"]