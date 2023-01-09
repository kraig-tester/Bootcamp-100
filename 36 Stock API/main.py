import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

av_url = "https://www.alphavantage.co/query"
av_api = "av_token"
av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": av_api
}

response = requests.get(av_url, av_params)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]

data_list = [value for (key,value) in data.items()]

day_1 = float(data_list[0]["4. close"])
day_2 = float(data_list[1]["4. close"])

price_difference = day_1 - day_2

if price_difference > 0:
    direction = "🔺"
else:
    direction = "🔻"

percent_difference = price_difference/float(day_1)*100

if abs(percent_difference) > 1:
    twilio_sid = "twillio_sid"
    auth_token = "twillio_token"
    
    news_url = "https://newsapi.org/v2/everything"
    news_api = "news_token"

    news_params = {
        "qInTitle": COMPANY_NAME,
        "sortBy": "publishedAt",
        "language": "en",
        "apikey": news_api
    }

    news_response = requests.get(news_url, news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    
    articles = news_data["articles"][:3]
    
    headlines = [f"{STOCK}: {direction}{abs(round(percent_difference))}%\n Headline: {article['title']}\nBrief: {article['description']}" for article in articles]

    for item in headlines:
        print(item)

        #uncomment to send via sms
        # client = Client(twilio_sid, auth_token)
    
        # message = client.messages \
        #             .create(
        #                 body=item,
        #                 from_='+14245443418',
        #                 to='enter_phone_number'
        #             )

        # print(message.status)
