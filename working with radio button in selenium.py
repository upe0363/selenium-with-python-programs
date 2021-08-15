import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoRadio():
    def demo_radio_button(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        time.sleep(4)
        print(driver.find_element_by_id("doi0").is_selected())
        driver.find_element_by_id("doi0").click()
        time.sleep(4)
        print(driver.find_element_by_id("doi0").is_selected())
        driver.find_element_by_id("doi1").click()
        print(driver.find_element_by_id("doi0").is_selected())
        print(driver.find_element_by_id("doi1").is_selected())
        time.sleep(4)

radiodemo = DemoRadio()
radiodemo.demo_radio_button()
