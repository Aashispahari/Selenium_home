from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
url = "https://sagar-test-qa.vercel.app/"

#to get to url
driver.get(url)
time.sleep(2)

#find elements
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, "//*[@id='loginForm']/button")

#action 
username.send_keys("Amrit")
time.sleep(2)
password.send_keys("Poudel")
time.sleep(2)
login_button.click()
time.sleep(3)



driver.quit