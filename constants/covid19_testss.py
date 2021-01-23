from selenium import webdriver
driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch(driver):
    driver.get("https://www.covid19india.org/")
    driver.maximize_window()
launch(driver)

