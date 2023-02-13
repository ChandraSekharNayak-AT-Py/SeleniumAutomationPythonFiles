from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://www.wikipedia.org/')

driver.find_element(By.NAME,"search").send_keys('India')
driver.find_element(By.XPATH,"//button[@type='submit']").click()
msg = driver.find_element(By.XPATH,"//table/tbody/tr[7]/td/a").text
print(msg)

time.sleep(10)
driver.close()