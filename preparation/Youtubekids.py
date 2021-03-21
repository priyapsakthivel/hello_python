import time

from selenium import webdriver
driver=webdriver.Edge("P:/Webdrivers/edgedriver.exe")
def launch(driver):
    driver.get("https://www.youtubekids.com/")
    driver.maximize_window()
launch(driver)
time.sleep(3)
def i_am_parent(driver):
    driver.find_element_by_id("parent-button").click()
    driver.find_element_by_id("next-button").click()
i_am_parent(driver)
time.sleep(2)
def hi_parent(driver):
    driver.find_element_by_id("digits-input").send_keys("1997")
hi_parent(driver)