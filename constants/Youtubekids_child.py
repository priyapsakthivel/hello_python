import time

from selenium import webdriver
driver = webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch(driver,time):
    driver.get("https://www.youtubekids.com/")
    driver.maximize_window()
    time.sleep(5)
launch(driver,time)

def choose_kids(driver,time):
    driver.find_element_id("kid-button").click()
    time.sleep(2)
choose_kids(driver,time)