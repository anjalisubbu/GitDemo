from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.maximize_window()

driver.get("https://login.salesforce.com/?locale=in")


driver.find_element_by_css_selector('#username').send_keys("Anjali")
driver.find_element_by_css_selector('.password').send_keys("123456789")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//div[@id='usernamegroup']/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)