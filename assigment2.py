from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://sagar-test-qa.vercel.app/about.html"
driver.get(url)
time.sleep(2)

#find elements
username = driver.find_element(By.ID, "fullname")
phone= driver.find_element(By.ID, "phone")
email = driver.find_element(By.ID,"email")
hobby = driver.find_element(By.ID, "hobby")
Submit_button = driver.find_element(By.XPATH, "//*[@id='aboutForm']/button")

#action 
username.send_keys("Aashish")
time.sleep(2)

phone.send_keys("9806647455")
time.sleep(2)

email.send_keys("test@email.com")
time.sleep(2)

hobby.send_keys("Reading")
time.sleep(2)

Submit_button.click()
time.sleep(3)

assert "fullname" in driver.current_url, "submission failed"
print("Submission Sucessfull")

driver.quit