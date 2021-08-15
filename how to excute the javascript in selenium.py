import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoJavascript():
    def demo_JavaScript(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.execute_script("window.open('https://training.rcvacademy.com/', '_self');")
        time.sleep(4)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", demo_element)

demojs = DemoJavascript()
demojs.demo_JavaScript()

