from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element_by_name("name").send_keys("Anjali")
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

assert "Copyright © ProtoCommerce 2018" == driver.find_element_by_xpath("//p[text()='Copyright © ProtoCommerce 2018']").text

driver.close()