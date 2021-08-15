import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoMultiWindow():
    def demo_windows(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH,"//a[@title='Web Check-in']//img[@class='conta iner large-banner']").click()
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH,"//a[@href='https://www.singaporeair.com/en_UK/plan-and-book/your-booking/checkin/']").click()
                time.sleep(4)
                driver.close()
                time.sleep(2)
                break
        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//a[@title='Web Check-in']//img[@class='conta iner large-banner']").click()


dmultiplewindows = DemoMultiWindow()
dmultiplewindows.demo_windows()