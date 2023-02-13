from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import traceback
import time

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver.implicitly_wait(5)
# print(dir(webdriver))
#url lunch
driver.get('https://rahulshettyacademy.com/angularpractice/')

#get page title
print(driver.title)
# driver.quit() # all window close using quite
# only current single window

#locaters
#id,name,cssname,xpath,link_text,class_name,tag_name,css selector

try:
    user_name = driver.find_element(By.CSS_SELECTOR,"input[name='na']")#Name
    user_name.send_keys('Krishna')

except NoSuchElementException:
    print(traceback.format_exc())


# driver.find_element(By.CSS_SELECTOR,"input[name='nam']").send_keys('Krishna')
driver.find_element(By.NAME,"email").send_keys("krishn108@gmail.com")#email
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234567")#password
driver.find_element(By.ID,"exampleCheck1").click()#check box


#Xpath and CSS_SELECTOR
#//tagname[@attribute='value']
#CSS:-  tagname[attribute='value'] #id, .classname

driver.find_element(By.XPATH,"//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME,"alert-success").text # sucess message
print(message)

assert 'Success' in message

time.sleep(5)
driver.close()