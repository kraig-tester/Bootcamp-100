import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 45.039268 # Your latitude
MY_LONG = 38.987221 # Your longitude
MY_EMAIL = "test@email.com"
MY_PASSWORD = "enter_password"

#If the ISS is close to my current position
def iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


# and it is currently dark
def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True

    return False


while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    # Then send me an email to tell me to look up.
    if iss_nearby() and is_night():
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(MY_EMAIL, MY_PASSWORD)
        #     connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look Up!\n\nThe ISS is above you in the sky.")

        print("Look Up!\n\nThe ISS is above you in the sky.")




