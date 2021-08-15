import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoDragDrop():
    def drag_drop(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        elem1 = driver.find_element(By.ID, "draggable")
        elem2 = driver.find_element(By.ID, "droppable")
        #ActionChains(driver).drag_and_drop(elem1, elem2).perform()
        ActionChains(driver).drag_and_drop_by_offset(elem1,  60 , 100).perform()
        time.sleep(4)


dd = DemoDragDrop()
dd.drag_drop()
