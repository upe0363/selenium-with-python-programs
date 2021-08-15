import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        #driver.find_element(By.CLASS_NAME, 'email-login-box').send_keys('rcv@rcvacademy.com')
        driver.find_element(By.ID, 'login-input').send_keys('rcv@rcvacademy.com')
        time.sleep(4)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()
