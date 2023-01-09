from twilio.rest import Client
import smtplib
import requests

TWILIO_SID = "enter_twillio_sid"
TWILIO_AUTH_TOKEN = "enter_twillio_token"

SHEETY_ENDPOINT = "enter_sheety_url"
SHEETY_KEY = "enter_sheety_token"

EMAIL = "test@gmail.com"
E_PASSWORD = "password"

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.headers = {
            "Authorization": f"Bearer {SHEETY_KEY}"
        }

    def send_deal(self, message):
        contents = message
        print(contents)
        # uncomment to send via sms
        # client = Client(twilio_sid, auth_token)
    
        # message = client.messages \
        #             .create(
        #                 body=contents,
        #                 from_='+14245443418',
        #                 to='enter_valid_number'
        #             )

        # print(message.status)

    
    def send_emails(self, message):
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(EMAIL, E_PASSWORD)
            
        #     response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)
        #     emails_data = response.json()["users"]

        #     for email in emails_data:
        #         print(f"Sending to {email['email']}")
        #         connection.sendmail(
        #             from_addr=EMAIL, 
        #             to_addrs=email, 
        #             msg=f"Subject:Happy Birthday!\n\n{message}"
        #         )

        response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)
        print(response.json())
        emails_data = response.json()["users"]
        for email in emails_data:
            print(f"Email: {email['email']}. Message: {message}")