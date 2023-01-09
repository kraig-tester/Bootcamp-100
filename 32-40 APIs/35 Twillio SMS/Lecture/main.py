import requests
from twilio.rest import Client
import os
# from twilio.http.http_client import TwilioHttpClient
# import pyperclip

WEATHER_API_3_HOUR_STEP = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "weather_token"

MY_LAT = 45.039268 
MY_LONG = 38.987221 

PARAMETERS_API = {
    "appid": API_KEY,
    "lat": MY_LAT,
    "lon": MY_LONG
}

TWILIO_SID = "twillio_sid"
AUTH_TOKEN = "twillio_token"


response = requests.get(WEATHER_API_3_HOUR_STEP, params=PARAMETERS_API)
response.raise_for_status()

data = response.json()

#taking 3 * 4 hours
weather_data = data["list"][:4]

# pyperclip.copy(str(weather_data))
# print(weather_data)

for time_item in weather_data:
    is_raining = False
    #simplified
    wether_id_per_period = time_item["weather"][0]["id"]
    # print(wether_id_per_period)
    if wether_id_per_period < 700:
        is_raining = True
        break

if is_raining:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(TWILIO_SID, AUTH_TOKEN)
    
    message = client.messages \
                .create(
                     body="It's going to rain today. Bring an umbrella with you.",
                     from_='+14245443418',
                     to='enter_valid_phone_number'
                 )

    print(message.status)


