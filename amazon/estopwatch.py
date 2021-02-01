import time

from selenium import webdriver
driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch(driver):
    driver.get("https://www.estopwatch.net/")
    driver.maximize_window()
launch(driver)

def start(driver):
    driver.find_element_by_id("startButton").click()
    time.sleep(10)
    driver.find_element_by_id("stopButton").click()
    timing= driver.find_element_by_id("mainStopwatch")
    print(timing.text)
start(driver)