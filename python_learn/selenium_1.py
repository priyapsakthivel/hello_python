from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch():
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    driver.maximize_window()
launch()
def popclose():
    driver.find_element_by_id("at-cv-lightbox-close").click()
