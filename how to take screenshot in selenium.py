import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoScreenshot():
    def demo_screen_capture(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        continuedemo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continuedemo.screenshot(".\\test.png")
        continuedemo.click()
        time.sleep(2)
        driver.get_screenshot_as_file("D:\\selenium project\\selenium project\\learning selenium\\error.png")
        driver.save_screenshot(".\\test1.png")

ddscreenshot = DemoScreenshot()
ddscreenshot.demo_screen_capture()
