import time

from selenium import webdriver
driver = webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch(driver,time):
    driver.get("https://www.youtubekids.com/")
    driver.maximize_window()
    time.sleep(5)
launch(driver,time)

def choose_kids(driver,time):
    driver.find_element_by_id("kid-button").click()
    time.sleep(5)
    display_message=driver.find_element_by_xpath("//*[@id='flow-step-container']/ytk-kids-child-welcome-page-renderer/div/h1").text
    print(display_message)
    driver.find_element_by_id("ok-button").click()
choose_kids(driver,time)