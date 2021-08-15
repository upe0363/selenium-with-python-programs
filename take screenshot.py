import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_default")
driver.maximize_window()
driver.implicitly_wait(1)

driver.save_screenshot("./screenshot.123r.png")

driver.switch_to.frame("iframeResult")
driver.execute_script("myFunction()")
driver.switch_to.default_content()

frames = driver.find_elements_by_tag_name("iframe")

for frame in frames:
    print(frame.get_attribute("id"))

print(len(frames))
