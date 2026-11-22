from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
url = "https://sagar-test-qa.vercel.app/contact.html"
driver.get(url)
driver.maximize_window()

#findelements
username = driver.find_element(By.ID, "name")
email = driver.find_element(By.ID, "email")
message = driver.find_element(By.ID, "message")
submit_button = driver.find_element(By.XPATH, "//*[@id='contactForm']/button")

# Contact_email = driver.find_element(By.XPATH, "/html/body/div/article/ul/li[1]/a")
# Linkdin = driver.find_element(By.XPATH, "/html/body/div/article/ul/li[3]/a")
# twitter = driver.find_element(By.XPATH, "/html/body/div/article/ul/li[4]/a")

username.send_keys("Pransa")
time.sleep(1)

email.send_keys("example@gmail.com")
time.sleep(1)

message.send_keys("Automation test")
time.sleep(1)

submit_button.click()
time.sleep(2)

assert "Pransa" in driver.current_url, "Submission failed"
print("Submission successfull")
# Contact_email.click()
# time.sleep(2)


# Linkdin.click()
# time.sleep(2)

# twitter.click()
# time.sleep(2)



driver.quit()