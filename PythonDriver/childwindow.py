from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
driver.switch_to.window(driver.window_handles[1])
assert "New Window" == (driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
assert  "Opening a new window" == driver.find_element_by_tag_name("h3").text
driver.close()