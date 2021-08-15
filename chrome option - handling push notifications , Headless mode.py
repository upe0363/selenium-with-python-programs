import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options = webdriver.ChromeOptions()

prefs = {"prifile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

#driver.get("https://www.redbus.in/")
driver.get("https://www.google.in/")
driver.maximize_window()

print(driver.title)