from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
driver.find_element_by_css_selector("a[href*='shop']").click()
#//div[@class='card h-100']/div/h4
products = driver.find_elements_by_xpath("//div[@class='card h-100']")


for product in products:
    product_name = product.find_element_by_xpath("div/h4/a").text
    if product_name == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()

assert product_name == driver.find_element_by_link_text("Blackberry").text
assert "In Stock" == driver.find_element_by_css_selector(".text-success").text

driver.find_element_by_css_selector("#exampleInputEmail1").clear()
driver.find_element_by_css_selector("#exampleInputEmail1").send_keys("2")
#price = driver.find_element_by_xpath("//strong[contains(text(),'₹. 50000')]").text
#Total = driver.find_element_by_class_name("text-right").text

driver.find_element_by_css_selector("button[class='btn btn-danger']").click()

Total = driver.find_element_by_css_selector(".text-right").text

if Total == "₹. 0":
    driver.find_element_by_css_selector("button[class='btn btn-default']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")


for product in products:
    product_name = product.find_element_by_xpath("div/h4/a").text
    if product_name == "iphone X":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class ='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[class='btn btn-success btn-lg']").click()
assert "Success! Thank you!" in driver.find_element_by_css_selector("div[class*='alert-success']").text



