from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

#user_name = input("Enter your IG Username: ")
#user_pass = input("Enter your IG Password: ")

driver = webdriver.Chrome(PATH)
#driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get("https://instagram.com")

time.sleep(3)

username = driver.find_element_by_name("username")
#username.send_keys(user_name)
username.send_keys("junayeed_")
password = driver.find_element_by_name("password")
#password.send_keys(user_pass)
password.send_keys("ComputerScience")
username.send_keys(Keys.RETURN)
time.sleep(3)

noSave = driver.find_element_by_class_name("cmbtv")
noSave.click()
#time.sleep(10)

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))).click()

driver.implicitly_wait(10)
for i in range(1000):
    driver.execute_script("window.scrollBy(0, 1)")
time.sleep(10)

driver.quit()