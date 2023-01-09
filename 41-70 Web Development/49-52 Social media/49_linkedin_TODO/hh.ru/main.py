import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

hh_url = "https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&excluded_text=&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50"
chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(hh_url)

driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div[1]/div/div/div/div[6]/a')

time.sleep(60)

driver.quit()
