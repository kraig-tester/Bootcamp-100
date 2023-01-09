from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "enter_path_to_chrome_driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

dates = [element.text for element in driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li time")]
names = [element.text for element in driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li a")]

events = {str(item):(dates[item],names[item]) for item in range(len(names)-1)}

print(events)

driver.quit()