from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://www.google.com/"
driver.get(url)
time.sleep(1)

driver.get("https://www.mindrisers.com.np/")
driver.refresh()
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

#error handeling and continuing the programm
try:
    assert driver.current_url == "https://www.mindrisers.com.np/", "Redirection failed"
    print(f"The current url is {driver.current_url}") 

except AssertionError as e:
    print (f"{e}")
    print("Continuing the program")



try:
    assert driver.title == "Best I Training Institute in kathmandu, Nepal | Mindrisers Institute of Technology"
    print(f"In right tittle page")

except AssertionError:
    print("Your are in wrong page")


driver.quit()

