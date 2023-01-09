import requests
from datetime import datetime
# from urllib.request import urlopen

MY_LAT = 45.039268
MY_LNG = 38.987221
# response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
# response_iss.raise_for_status()

# data = response_iss.json()

# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]

# print(f"latitude: {latitude}\nlongitude: {longitude}")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0 
}
response_sun = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
response_sun.raise_for_status()

data = response_sun.json()

# print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")
sunset = data["results"]["sunset"].split("T")[1].split(":")

print(sunrise)
print(sunset)

sunrise_hour = sunrise[0]
sunrise_minutes = sunrise[1]

sunset_hour = sunset[0]
sunset_minutes = sunset[1]

time_now = datetime.now()

print(f"Sunrise: {sunrise_hour}\nSunset: {sunset_hour}\nNow: {time_now.hour}")

