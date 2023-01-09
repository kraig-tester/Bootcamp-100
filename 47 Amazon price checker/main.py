import requests
import smtplib
from bs4 import BeautifulSoup
import lxml


email = "enter_valid_email"
password = "email_password"
product_to_track = "https://www.amazon.ca/Console-3005718-PlayStation-5/dp/B08FC5L3RG/ref=sr_1_1?crid=3NJZFY5VZK3SC&keywords=playstation+5&qid=1668532199&qu=eyJxc2MiOiI0LjU3IiwicXNhIjoiNi42NCIsInFzcCI6IjYuNzQifQ%3D%3D&sprefix=playstation%2Caps%2C469&sr=8-1"
desired_price = 1000

def send_email(contents):
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
                from_addr=email, 
                to_addrs=email, 
                msg=f"Subject:Amazon price checker alert.\n\n{contents}"
            )
    except:
        print(contents)
        return False
    else:
        return True

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0 (Edition Yx 05)",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=product_to_track, headers=header)
soup = BeautifulSoup(response.text, "lxml")

#PlayStation 5
product_name = name=soup.find("span", class_="product-title-word-break").getText().strip()

#1350.
current_price_whole = soup.find(name="span", class_="a-price-whole").getText().split(",")
current_price_whole = current_price_whole[0] + current_price_whole[1]
#97
current_price_decimal = soup.find(name="span", class_="a-price-fraction").getText()

current_price = float(current_price_whole+current_price_decimal)
if current_price < desired_price:
    contents = f"Price for {product_name} dropped below desired price of ${desired_price}, \nCurrent price is ${current_price}"
    send_email(contents)
