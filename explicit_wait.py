from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

#Assertion check for product

excepted_prodcut = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
final_prodcut = []

result_prodcuts = driver.find_elements(By.XPATH,"//div[@class='products']/div")

for product in result_prodcuts:
    final_prodcut.append(product.find_element(By.XPATH,'h4').text)

assert excepted_prodcut == final_prodcut

count = len(result_prodcuts)
assert count > 0

#selenium chaining
for result in result_prodcuts:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#Sum Validation
product_prices=  driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
# print(len(product_prices))
sum = 0
for price in product_prices:
    sum = sum+int(price.text)
total_amount = driver.find_element(By.CSS_SELECTOR,".totAmt").text
assert sum == int(total_amount)




wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

msg = driver.find_element(By.CLASS_NAME,"promoInfo").text
print(msg)

driver.close()

