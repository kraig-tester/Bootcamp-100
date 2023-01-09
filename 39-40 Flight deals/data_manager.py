import requests

SHEETY_ENDPOINT = "enter_sheety_url"
SHEETY_KEY = "enter_sheety_key"

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "Authorization": f"Bearer {SHEETY_KEY}"
        }

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)

        self.destination_data = response.json()["prices"]
        return self.destination_data
        
            
    def update_destination_codes(self):
        for city in self.destination_data:   
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }

            response = requests.put(url=SHEETY_ENDPOINT + f"/{city['id']}", headers=self.headers, json=new_data)
            response.raise_for_status()
            print(response.text)
