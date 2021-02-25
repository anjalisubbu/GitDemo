from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/frames")
assert "Frames" == driver.find_element_by_tag_name("h3").text
driver.find_element_by_link_text("iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Handled frames successfully")
driver.switch_to.default_content()
driver.find_element_by_css_selector("button[id='mceu_15-open'] i").click()
action = ActionChains(driver) #mouse hover
action.move_to_element(driver.find_element_by_css_selector("#mceu_32")).click().perform()
#action.move_to_element(menu).click().perform()
driver.switch_to.frame("mce_0_ifr")
assert "" == driver.find_element_by_css_selector("#tinymce").text
driver.switch_to.default_content()
assert "An iFrame containing the TinyMCE WYSIWYG Editor" == driver.find_element_by_tag_name("h3").text

