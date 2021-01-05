import time

from selenium import webdriver

driver = webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch(driver):
    driver.get("https://www.youtubekids.com/")
    driver.maximize_window()
    time.sleep(7)
launch(driver)
time.sleep(7)

def choose_parents(driver,time):
    driver.find_element_by_id("parent-button").click()
    driver.find_element_by_id("next-button").click()
    time.sleep(2)
choose_parents(driver,time)