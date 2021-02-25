

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Anjali")
driver.find_element_by_css_selector("[name ='email']").send_keys("anjalikavathar@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("123456")
driver.find_element_by_xpath("//input[@type='checkbox']").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))

dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value("M")

driver.find_element_by_css_selector("[value ='Submit']").click()
print(driver.find_element_by_css_selector("[class*='alert-success']").text)