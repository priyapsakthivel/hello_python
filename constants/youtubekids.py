import time

from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch(driver):
    driver.get("https://www.youtubekids.com/")
    driver.maximize_window()
    driver.find_element_by_id()
launch(driver)
time.sleep(7)

def choose_kids(driver):
    driver.find_element_by_id("kid-button").click()
    time.sleep(5)
    driver.find_element_by_id("ok-button").click()
    time.sleep(2)
choose_kids(driver)