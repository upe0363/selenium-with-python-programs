from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.w3schools.in/html-tutorial/")
driver.maximize_window()
driver.implicitly_wait(1)

print(driver.find_element_by_xpath("//*[@id=\"leftMenu\"]/div[2]/a[1]").value_of_css_property("font"))

print(driver.find_element_by_xpath("//*[@id=\"leftMenu\"]/div[2]/a[1]").value_of_css_property("color"))

print(driver.find_element_by_xpath("//*[@id=\"leftMenu\"]/div[2]/a[1]").value_of_css_property("font-family"))