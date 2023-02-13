from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

#Dynamic Checkbox
check_box = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(check_box))

for check in check_box:
    if check.get_attribute("value") == "option2":
        check.click()
        assert  check.is_selected()

#Static Radion Button
radio_button = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radio_button[2].click()
time.sleep(5)

driver.close()