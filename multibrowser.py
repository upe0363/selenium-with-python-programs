from selenium import webdriver
from selenium.webdriver.common.keys import keys

#driver = webdriver.chrome(exexcutable_path="C:\Users\DELL\Desktop\chromedriver.exe")
driver=webdriver.firefox(executable_path="C:\Users\DELL\Desktop\geckodriver.exe")
driver.get("http://newtours.demoaut.com/")

print(driver.title)#title of the page

driver.closer()