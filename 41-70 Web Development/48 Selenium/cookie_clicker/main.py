import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

cookie_clicker_url = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = "enter_path_to_chrome_driver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(cookie_clicker_url)

print(time.time())

timeout = 300
timeout_start = time.time()
time_for_upgrade = timeout_start + 5

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

while time.time() < timeout_start + timeout:
    cookie.click()

    most_expensive_price = 0
    most_expensive_element = None
    
    if time.time() > time_for_upgrade:
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")
    
        for upgrade in upgrades:
            if upgrade.get_attribute("class")=="grayed" or upgrade.get_attribute("class")=="amount":
                continue
            
            upgrade_price = int(upgrade.find_element(By.CSS_SELECTOR, "b" ).text.replace(",", "").split()[2])

            if most_expensive_element == None or upgrade_price > most_expensive_price:
                most_expensive_price = upgrade_price
                most_expensive_element = upgrade
        if most_expensive_element != None:
            most_expensive_element.click()
            time_for_upgrade = time.time() + 5

time.sleep(10)

cps = driver.find_element(By.ID, "cps").text.split()[2]

print(f"Your cps(cookies per second was {cps}")

driver.quit()