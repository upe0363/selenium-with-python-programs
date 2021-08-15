import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Demoframes():
    def demo_frames(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        #switch with iframe locator
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='iframeResult']"))
        #SWITCH with ID
        driver.switch_to.frame("iframeResult")
        #switch with name
        driver.switch_to.frame("iframeResult")
        #switch with index
        driver.switch_to.frame(0)

        driver.find_element(By.XPATH, "//a[@class='w3-button w3-block'][normalize-space()='Paid Courses']").click()

diframe = Demoframes()
diframe.demo_frames()