from selenium import webdriver

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/")
print(driver.title)
driver.back()
driver.get("https://rahulshettyacademy.com/#/practice-project")
driver.minimize_window()
print(driver.title)
print("Successful launch")
#driver.close()