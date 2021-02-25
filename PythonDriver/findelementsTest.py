import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys('aus')
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[role='presentation'] a")
print(len(countries))
for country in countries:
    if country.text == "Austria":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").get_attribute('value'))
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "Austria"