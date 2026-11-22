from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com/buttons"
driver.get(url)

primary = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div/div/button[1]")

try:
    primary.click()
    print("primary button clicked")

except Exception :
    print("Primary button not clicked")

dropdown  = driver.find_element (By.ID, "btnGroupDrop1")

try:
    dropdown.click()
    print("Dropdown button clicked")

except Exception :
    print("Dropdown button not clicked")



time.sleep(3)

driver.quit()