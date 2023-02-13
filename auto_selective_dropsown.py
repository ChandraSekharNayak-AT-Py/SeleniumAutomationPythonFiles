from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element(By.ID,"autosuggest").send_keys('ind')
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "India":
        country.click()
        break

time.sleep(10)


#Validate get-Dynamic Texts
# msg = driver.find_element(By.XPATH,"(//span[@class='text-label'])[1]").text
# print(msg)

msg = driver.find_element(By.ID,"autosuggest").get_attribute("value")
print(msg)

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"

driver.close()

#https://rahulshettyacademy.com/practice-project
