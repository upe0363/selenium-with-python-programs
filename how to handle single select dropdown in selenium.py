import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


class DemoDropdownSingleSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/au/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dropdown = driver.find_element_by_name("UserTitle")
        dd = Select(dropdown)

        dd.select_by_index(1)
        time.sleep(3)

        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(3)

        dd.select_by_value("CxO_General_Manager_ANZ")
        time.sleep(3)

dddemo = DemoDropdownSingleSelect()
dddemo.demo_dropdown()

