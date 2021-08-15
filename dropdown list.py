import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.wikipedia.org/")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
#English - US English - UK

# driver.find_element_by_id("searchLanguage").send_keys("English")

dropdown = driver.find_element_by_id("searchLanguage")
select = Select(dropdown)
#select.select_by_visible_text("Eesti")
select.select_by_value("simple")

options = driver.find_elements_by_tag_name("option")

for option in options:
    print("Text is : ",option.text, "Lang is : "+option.get_attribute("lang"))

print("Total dropdown values are ",len(options))




