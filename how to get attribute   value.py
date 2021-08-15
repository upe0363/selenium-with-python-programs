import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoGetattibuteValue():
    def demo_getvalue(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        #attr_value = driver.find_element_by_xpath("//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        attr_value = driver.find_element_by_xpath("//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("type")
        print(attr_value)
        time.sleep(4)

attrobj = DemoGetattibuteValue()
attrobj.demo_getvalue()