import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Program Files\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3328888455&distance=25&f_AL=true&f_WT=1&geoId=103644278&keywords=python%20junior%20developer")

# sign_in = driver.find_element(By.CSS_SELECTOR, ".nav .nav__cta-container .nav__button-secondary")
sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

session_key = driver.find_element(By.NAME, 'session_key')
session_key.send_keys('ikrasnyanskiy@myseneca.ca')
session_password = driver.find_element(By.NAME, 'session_password')
session_password.send_keys('XNxj$fFF%37&#rt')
submit_btn = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
submit_btn.click()

time.sleep(60)

driver.quit()