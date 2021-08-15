from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://www.gmail.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_id("identifierId").send_keys("upendra.singh0363@gmail.com")
driver.find_element_by_xpath("//span[normalize-space()='Next']").click()
#time.sleep(3)

driver.find_element_by_xpath("//*id=\"password\"]/div[1]/div/[1]/input").send_keys("asdsdsds")

driver.find_element_by_xpath("//*[@id=\"passwordNext\]div/button/div[2]").click()