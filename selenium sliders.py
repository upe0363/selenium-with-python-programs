from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
driver.implicitly_wait(10)

slider = driver.find_element_by_xpath("//*[@id=\"slider\"]/span")

ActionChains(driver).drag_and_drop_by_offset(slider,400,0).perform()
