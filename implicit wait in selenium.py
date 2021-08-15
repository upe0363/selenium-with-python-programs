import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoImplicitWait():
    def demo_imp_wait(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=au")
        driver.find_element(By.ID, "username").send_keys("RCV Academy")
        driver.find_element(By.ID, "password").send_keys("RCV Academy")
        time.sleep(5)

impwait =  DemoImplicitWait()
impwait.demo_imp_wait()