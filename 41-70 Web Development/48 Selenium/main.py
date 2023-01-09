import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "enter_path_to_chrome_driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

docs = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(docs.text)

bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# closes tab
# driver.close()

#closes browser
driver.quit()