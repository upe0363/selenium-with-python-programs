from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(10)

draggable = driver.find_element_by_id("draggable")
droppable = driver.find_element_by_id("droppable")

ActionChains(driver).drag_and_drop("draggable,droppable").perform()

