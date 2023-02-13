# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# service_obj = Service("C:\\ChromeDriver\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get('https:/rahulshettyacademy.com/client')
#
# # driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"password?").click()
# # //tagname[@attribute='value']
#
# # driver.find_element(By.XPATH,"//input[@type='email']").send_keys('demo@gmail.com') #relativeble xpath
# driver.find_element(By.XPATH,'//form/div[1]/input').send_keys('demo@gmail.com') #absolute xpath
# driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys('12345666')
# driver.find_element(By.CSS_SELECTOR,'#confirmPassword').send_keys('12345666')
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# time.sleep(10)
#
# driver.close()

