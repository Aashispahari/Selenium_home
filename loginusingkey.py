from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
url = "https://www.saucedemo.com/"
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
login_button =wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

username.send_keys("standard_user")
time.sleep(2)
action.send_keys(Keys.TAB).perform()

action.send_keys("secret_sauce")
time.sleep(2)
action.send_keys(Keys.TAB).perform()
time.sleep(2)
action.send_keys(Keys.ENTER).perform()

time.sleep(2)
driver.quit()