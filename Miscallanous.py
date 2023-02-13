from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

time.sleep(5)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.execute_script(("window.scrollBy(0,500)"))
driver.get_screenshot_as_file("screen_shot_1.png")


time.sleep(3)
driver.close()
