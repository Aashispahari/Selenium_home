from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
url = "https://sagar-test-qa.vercel.app/"

#to get to url
driver.get(url)

wait = WebDriverWait(driver,10)

#find elements
# username = driver.find_element(By.ID, "username")
username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
# password = driver.find_element(By.ID, "password")
password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
# login_button = driver.find_element(By.XPATH, "//*[@id='loginForm']/button")
login_button =  wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='loginForm']/button")))


#action 
username.send_keys("Amrit")
time.sleep(2)
password.send_keys("Poudel")
time.sleep(2)
login_button.click()

time.sleep(3)
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)


driver.quit