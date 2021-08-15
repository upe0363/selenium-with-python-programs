import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoMouseOver():
    def demo_mouse_events(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        morebutton = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        myaccount_link = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        achains = ActionChains(driver)
        achains.move_to_element(myaccount_link).perform()
        time.sleep(3)
        achains.move_to_element(morebutton).perform()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
        time.sleep(5)

dmouse = DemoMouseOver()
dmouse.demo_mouse_events()