from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://mathup.com/games/crossbit')
driver.implicitly_wait(5)
plays = driver.find_element(By.XPATH,"//div[@class='GamePreStart_btn__S9w8W btn ']")

count = 10
while count > 1:
    plays.click()
    result = driver.find_element(By.XPATH, "(//div[@class='GamePostStart_value__zH0b9'])[2]").text
    print(result)
    count = count -1

time.sleep(5)
driver.close()