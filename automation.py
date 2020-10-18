from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

user_name = input("Enter your IG Username: ")
user_pass = input("Enter your IG Password: ")

driver = webdriver.Chrome(PATH)
driver.get("https://instagram.com")

time.sleep(5)

username = driver.find_element_by_name("username")
username.send_keys(user_name)
password = driver.find_element_by_name("password")
password.send_keys(user_pass)
username.send_keys(Keys.RETURN)

time.sleep(10)

driver.quit()