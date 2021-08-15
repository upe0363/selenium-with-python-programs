import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoCheckboxes():
    def demo_checkbox(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        driver.find_element_by_id("interest_market_c0").click()
        time.sleep(4)
        var1 = driver.find_element_by_id("interest_market_c0").is_selected()
        print(var1)
        driver.find_element_by_id("interest_sell_c0").click()
        time.sleep(4)
        var2 = driver.find_element_by_id("interest_sell_c0").is_selected()
        print(var2)


checkbox =DemoCheckboxes()
checkbox.demo_checkbox()