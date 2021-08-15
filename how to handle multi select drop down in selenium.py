import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class DemoDropdownMultiSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
        dd_demo = driver.find_element_by_id("multi-select")
        dd_multi = Select(dd_demo)

        dd_multi.select_by_index(0)
        dd_multi.select_by_value("New Jersey")
        dd_multi.select_by_visible_text("Florida")
        dd_multi.select_by_index(3)
        dd_multi.select_by_value("Ohio")
        dd_multi.select_by_visible_text("Texas")
        time.sleep(3)
        dd_multi.deselect_by_index(0)
        dd_multi.deselect_by_value("New Jersey")
        dd_multi.deselect_by_visible_text("Florida")
        time.sleep(3)
        dd_multi.deselect_all()
        time.sleep(4)


demo_multiselect = DemoDropdownMultiSelect()
demo_multiselect.demo_dropdown()
