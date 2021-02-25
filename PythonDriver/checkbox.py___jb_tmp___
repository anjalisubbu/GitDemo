import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkbox))

for options in checkbox:
#    if options.get_attribute("value") == "options2":
        options.click()

        #assert options.is_selected()
dropdown =Select(driver.find_element_by_css_selector("#dropdown-class-example"))
dropdown.select_by_value("option3")

driver.find_element_by_css_selector("input[id= 'autocomplete']").send_keys("Ind")
time.sleep(2)
listofoptions = driver.find_elements_by_css_selector("li[class='ui-menu-item'] div")
print(len(listofoptions))

for list in listofoptions:
    if list.text == "India":
        list.click()
        break

radio = driver.find_elements_by_name("radioButton")
radio[2].click()

validationText = "Anjali"
driver.find_element_by_css_selector("#name").send_keys(validationText)
time.sleep(2)
driver.find_element_by_css_selector("#alertbtn").click()
alert = driver.switch_to.alert
message = alert.text
assert validationText in message
time.sleep(2)
alert.accept()
driver.find_element_by_css_selector("#confirmbtn").click()
time.sleep(2)
alert.dismiss()


print(driver.find_element_by_xpath("//legend[text()='Checkbox Example']").text)
print(driver.find_element_by_xpath("//legend[text()='Switch To Alert Example']").text)

time.sleep(2)

assert driver.find_element_by_css_selector("#displayed-text").is_displayed()
driver.find_element_by_css_selector("#hide-textbox").click()
assert not driver.find_element_by_css_selector("#displayed-text").is_displayed()

driver.close()