import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoGetText():
    def demo_gettext(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        text = driver.find_element_by_xpath("//p[contains(text(),'Tirupati Darshan: 10 Interesting Facts You Must Kn')]").text
        text1 = driver.find_element_by_link_text('Yatra for Business').text
        print(text1)
        time.sleep(4)

findbyid =DemoGetText()
findbyid.demo_gettext()