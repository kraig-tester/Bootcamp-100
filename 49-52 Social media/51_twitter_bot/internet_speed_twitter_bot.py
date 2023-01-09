import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 100
PROMISED_UP = 100
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""
chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"


class InternetSpeedTwitterBot():


    def __init__(self) -> None:
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        start_element = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_element.click()

        time.sleep(45)

        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

        
    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com")
        sign_in = self.driver.find_element(By.CLASS_NAME, 'nsm7Bb-HzV7m-LgbsSe-Bz112c')
        sign_in.click()
        time.sleep(10)

        if self.down < PROMISED_DOWN:
            print(f"Your download speed is lower than anticipated.")
        elif self.up < PROMISED_UP:
            print(f"Your download speed is lower than anticipated.")
        elif self.down < PROMISED_DOWN and self.up < PROMISED_UP:
            print(f"Your download and upload speeds are lower than anticipated.")
        else:
            print("Your internet speed is running as expected.")
    