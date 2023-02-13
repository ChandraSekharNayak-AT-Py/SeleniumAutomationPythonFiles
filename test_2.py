from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/angularpractice/')


driver.find_element(By.NAME,'email').send_keys('k.csnyak108@gmail.com')
driver.find_element(By.ID,'exampleInputPassword1').send_keys('12345667')
driver.find_element(By.ID,'exampleCheck1').click()

#Select/Static Dropdown

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
time.sleep(5)
dropdown.select_by_index(1)


#CSS_SELECTOR(tagname[attribute='Value']) ,.classname,#id

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys('Krishna')
# driver.find_element(By.CSS_SELECTOR,".form-control").send_keys('Krishna')
# driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys(7867634)



#Xapth :- "//tagname[@attribute='Value']"
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,'alert-success').text
# print(message)

assert 'Success!' in message #validation (assertion checking)

#Two Way Data Binding

driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys('Automation')
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").clear()

time.sleep(10)

driver.close()

