import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoElementState():
    def demo_enable_disable(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        demo_state = driver.find_element_by_xpath("//input[@id='login_button']").is_enabled()
        print(demo_state)

        driver.find_element_by_xpath("//input[@id='user_name']").send_keys("testing")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='user_name']").send_keys("testing343")
        time.sleep(2)
        demo_state1 = driver.find_element_by_xpath("//input[@id='login_button']").is_enabled()
        print(demo_state1)


demostate =DemoElementState()
demostate.demo_enable_disable()