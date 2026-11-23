from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver  = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
url = "https://sagar-test-qa.vercel.app/contact.html"
driver.get(url)
driver.maximize_window()

username = wait.until(EC.visibility_of_element_located((By.ID, "name")))
username.send_keys("Amrit")

email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
email.send_keys("aashish@gmail.com")

message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
message.send_keys("Trying wait")

submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='contactForm']/button")))
submit_button.click()
time.sleep(2)



driver.quit()

