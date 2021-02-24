from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch():
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    driver.maximize_window()
launch()
def popclose():
    driver.find_element_by_id("at-cv-lightbox-close").click()
    driver.execute_script("scrollTo(0,100)")
popclose()
def message():
    driver.find_element_by_id("user-message").send_keys()
    driver

