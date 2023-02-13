from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,".search-keywor").send_keys("ber")
time.sleep(2)
result_prodcuts = driver.find_elements(By.XPATH,"//div[@class='products']/div")

count = len(result_prodcuts)
assert count > 0

#selenium chaining
for result in result_prodcuts:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

msg = driver.find_element(By.CLASS_NAME,"promoInfo").text
print(msg)


time.sleep(10)
driver.close()