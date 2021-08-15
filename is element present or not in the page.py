from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# method 1
##def is_element_present(id):
#    try:
#        driver.find_element_by_id(id)
 #       return true
 #   except NoSuchElementException:
 #       return False


# Method 2
#def is_element_present(how, what):
#    try:
  #      driver.find_elemets(by=how, value=what)
  #      return True
  #  except NoSuchException:
   #     return False


def is_element_present(how, what):
    if len(driver.find_elements(by=how, value=what)) == 0:
        return False
    else:
        return True


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://www.gmail.com")
driver.maximize_window()
driver.implicitly_wait(10)

#print(driver.find_element_by_id("identifierId").is_displayed())
#print(is_elemet_present("identifierId656"))
print(is_element_present(By.ID,"identifierId"))
print(is_element_present(By.XPATH,"//*[@id='identifierId']"))
