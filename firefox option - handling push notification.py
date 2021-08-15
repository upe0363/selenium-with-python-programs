import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

firefox_options = Options()

#firefox_options.set_preference("dom.webnotification.enabled", False)
firefox_options.set_preference("dom.webnotifications.enabled", False)
firefox_options.headless = True

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=firefox_options)

#driver.get("https://www.redbus.in/")
driver.get("https://www.google.in/")
driver.maximize_window()
time.sleep(4)
print(driver.title)
