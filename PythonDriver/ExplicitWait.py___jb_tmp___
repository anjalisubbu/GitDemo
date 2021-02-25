import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
time.sleep(5)
count = len(driver.find_elements_by_css_selector("div[class='product']"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
page1_list = []
page2_list = []

for options in buttons:
    page1_list.append(options.find_element_by_xpath("parent::div/parent::div/h4").text)
    options.click()

assert expected_list == page1_list

driver.find_element_by_css_selector("[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,"p.product-name"))

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoCode')))

veggies_in_page2 = driver.find_elements_by_css_selector("p.product-name")
for veggies in veggies_in_page2:
    page2_list.append(veggies.text)

print(page2_list)
assert page1_list == page2_list

total_amt = driver.find_elements_by_xpath("//tr/td[5]/p")

sum = 0
for amt in total_amt:
    sum = sum + int(amt.text)
print("Sum of all veggies:",sum)

sum_validation = int(driver.find_element_by_class_name("totAmt").text)

assert sum == sum_validation

original_amt = driver.find_element_by_css_selector(".discountAmt").text
print("Validation:" + original_amt)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element_by_class_name("promoInfo").text)
discount_amt = driver.find_element_by_css_selector(".discountAmt").text
print(discount_amt)

assert original_amt > discount_amt




#print(driver.find_element_by_css_selector(".discountPerc").text)

driver.close()