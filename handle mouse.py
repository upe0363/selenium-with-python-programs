import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://deluxe-menu.com/popup-mode-sample.html")
driver.maximize_window()
driver.implicitly_wait(10)

img = driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/p[2]")

ActionChains(driver).context_click(img).perform()

driver.find_element(By.XPATH, "//*[@id=\"dm2m1i1tdT\"]").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id=\"dm2m2i0tdT\"]").click()

# pur = driver.find_element_by_xpath("//*[@id=\"dm2m1i3tdT\"]").click()


