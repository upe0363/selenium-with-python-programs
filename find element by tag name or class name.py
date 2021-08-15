import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        #driver.find_element_by_tag_name('input').send_keys('upendra.com')
        driver.find_element_by_class_name('email-login-box').send_keys('upendra.com')
        time.sleep(4)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()
