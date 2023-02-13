from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')

#link_text
# driver.find_element(By.LINK_TEXT,"org.openqa.selenium.devtools.idealized.log").click() -- wrong approch

#Switch into frame
#switch_to.frame(name)
#switch_to.frame(id)

driver.switch_to.frame("packageListFrame") # First Frame
driver.find_element(By.LINK_TEXT,"org.openqa.selenium.devtools").click()
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame") #Frame-2
driver.find_element(By.LINK_TEXT,"Connection").click()
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")#Frame-3
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()
time.sleep(3)
driver.switch_to.default_content()



time.sleep(5)
driver.close()