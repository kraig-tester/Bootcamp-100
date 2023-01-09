import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "enter_path_to_chrome_driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# challenge 1
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# num_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(num_of_articles.text)
# # num_of_articles.click()

# news_link = driver.find_element(By.LINK_TEXT, "Russian invasion of Ukraine")
# print(news_link)
# # news_link.click()

# search_bar = driver.find_element(By.NAME, "search")
# # search_bar.click()
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

# challenge 2
driver.get("http://secure-retreat-92358.herokuapp.com")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Ig")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Kr")

email = driver.find_element(By.NAME, "email")
email.send_keys("igorsknakubani@gmail.com")

button = driver.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(5)

driver.quit()