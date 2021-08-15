import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.find_element_by_partial_link_text('holida').click()
        time.sleep(4)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()
