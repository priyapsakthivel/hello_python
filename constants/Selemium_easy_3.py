import time

from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch():
    driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
    driver.maximize_window()
    driver.find_element_by_id("isAgeSelected").click()
    message=driver.find_element_by_id("txtAge").text
    time.sleep(2)
    print(message)
    driver.get_screenshot_as_file("P:\screenshot\show"+message+".png")
launch()