from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def launching(driver):
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html");
    driver.maximize_window();
launching(driver)