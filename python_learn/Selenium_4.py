from selenium import webdriver

driver= webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def launch():
    driver.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
    driver.maximize_window()
    driver.execute_script("scrollTo(0,2500)")
launch()