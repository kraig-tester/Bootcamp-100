import requests
import datetime as dt
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

ORIGIN_IATA = "LON"
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

pprint("Checking destination list...")

if sheet_data[0]["iataCode"] == "":
    print("Uploading IATA codes...")
    for line in sheet_data:
        line["iataCode"] = flight_search.getCode(line["city"])
    
    # print(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
else:
    print("IATA Codes are up-to-date.")


tommorow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
six_month = (dt.datetime.now() + dt.timedelta(days=182)).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = flight_search.check_flights(ORIGIN_IATA,destination["iataCode"],tommorow,six_month)
    if flight != None and flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        if flight.stop_overs != 0:
            message += f"\n\nFlight has {flight.stop_overs} stop over, via {flight.via_city}"
        notification_manager.send_deal(message)
        notification_manager.send_emails(message)
        