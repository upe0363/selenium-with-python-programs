import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        #driver.find_element_by_tag_name('input').send_keys('upendra.com')
        #lista = driver.find_elements_by_tag_name('a')
        #lista = driver.find_elements_by_tag_name('input')
        #lista = driver.find_elements_by_tag_name('a')
        lista = driver.find_elements(By.TAG_NAME, 'a')
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(4)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()
