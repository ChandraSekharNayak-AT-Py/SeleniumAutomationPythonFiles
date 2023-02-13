from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjc0MDU1MTgzLCJjYWxsc2l0ZV9pZCI6MjY5NTQ4NDUzMDcyMDk1MX0%3D')
driver.find_element(By.XPATH,"//input[@id='email']").send_keys('7978390510')
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys('Gellu@03')
driver.find_element(By.XPATH,"//button[@id='loginbutton']").click()


time.sleep(20)

