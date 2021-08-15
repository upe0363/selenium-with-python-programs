import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoRightDoubleClick():
    def demo_right_double(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        # Right Click
        achains = ActionChains(driver)
        elem1 = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        copyelem = driver.find_element(By.XPATH, "//span[normalize-space()='copy']")
        achains.context_click(elem1).perform()
        time.sleep(3)
        copyelem.click()
        time.sleep(3)

drightclick = DemoRightDoubleClick()
drightclick.demo_right_double()

