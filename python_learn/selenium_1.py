from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch():
    driver.get("P:\Webdrivers\msedgedriver")
    driver.maximize_window()
launch()
