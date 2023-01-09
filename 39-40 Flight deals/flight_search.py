import requests
from flight_data import FlightData
from pprint import pprint

KIWI_ENDPOINT = "https://api.tequila.kiwi.com"
KIWI_KEY = "enter_kiwi_token"

class FlightSearch:

    
    def getCode(self, city):
        params = {
            "term": city,
            "location_types": "city"
        }
        headers = {
            "apikey": KIWI_KEY
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}/locations/query", params=params, headers=headers)
        response.raise_for_status()
        try:
            code = response.json()["locations"][0]["code"]
        except:
            code = "TESTING"
        # pprint(response.json())
        return code

    
    def check_flights(self, from_city, to_city, from_date, to_date):
        params = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        headers = { 
            "apikey": KIWI_KEY 
        }

        response = requests.get(url=f"{KIWI_ENDPOINT}/v2/search", params=params, headers=headers)
        response.raise_for_status()

        try:
             data = response.json()["data"][0] 
        except IndexError:
            params["max_stopovers"] = 1
            response = requests.get(url=f"{KIWI_ENDPOINT}/v2/search", params=params, headers=headers)
            response.raise_for_status()
            flight_data = response.json()["data"]
            if len(flight_data) != 0:
                data = flight_data[0]
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
            else:
                print(f"No flights available from {from_city}.")
                return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
        
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data