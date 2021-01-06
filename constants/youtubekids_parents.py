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

def hi_parents(driver,age):
    for x in range(1,5):
        driver.find_element_by_id("onboarding-age-gate-digit-"+str(x)).send_keys(age[age-1])
        time.sleep(30)
        driver.find_element_by_id("submit-button").click()
age=input("please enter your age parents")
hi_parents(driver,list(age))
