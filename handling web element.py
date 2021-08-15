import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.yatra.com/")
driver.maximize_window()

# Method 1
#username = driver.find_element_by_id("identifierId")
#username.send_keys("upendra.singh0363@gmail.com")

# Method 2
driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
driver.find_element_by_xpath("//a[normalize-space()='Login']").click()
time.sleep(4)
driver.find_element_by_xpath("//input[@id='login-input']").send_keys("upendra.singh0363@gmail.com")
driver.find_element_by_xpath("//button[@id='login-continue-btn']").click()
time.sleep(4)
driver.find_element_by_xpath("//input[@id='login-password']").send_keys("ssfusdfhfsjfjys")
driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
time.sleep(4)


#driver.find_elements_by_xpath("//input[@id='login-input']").send_keys("upendra.singh0363@gmail.com")
#driver.find_element_by_id("identifierID").send_keys("upendra.singh0363@gmail.com")