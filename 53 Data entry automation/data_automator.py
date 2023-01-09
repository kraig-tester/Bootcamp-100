import time
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

google_form = "enter_google_form_url"
ZILLOW_URL = "https://www.zillow.com"
zillow_search_result = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56872555187691%2C%22east%22%3A-122.35329052380074%2C%22south%22%3A37.67556604076504%2C%22north%22%3A37.83652956812414%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A505987%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2500%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
chrome_driver_path = "enter_path_to_chrome_driver"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0 (Edition Yx 05)",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


class DataAutomator():


    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.links = []
        self.prices = []
        self.addresses = []
    
    
    def get_prices(self):
        response = requests.get(headers=header ,url=zillow_search_result)
        soup = BeautifulSoup(response.text, "html.parser")
        listings = soup.select(selector="#search-page-list-container ul li") 
        for listing in listings:
            try:
                self.links.append(ZILLOW_URL + listing.find(name="a").get(key="href").replace(ZILLOW_URL, ''))
                self.prices.append(re.search("([0-9],+[0-9]*)", listing.select_one(selector="div div div span").getText()).group(1))
                self.addresses.append(listing.find(name="address").getText())
            except:
                continue


    def fill_forms(self):
        self.driver.get(google_form)
        
        for i in range(len(self.addresses)):
            time.sleep(2)
            address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            address.send_keys(self.addresses[i])
            price.send_keys(self.prices[i])
            link.send_keys(self.links[i])
            submit_button.click()

            send_another = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            send_another.click()