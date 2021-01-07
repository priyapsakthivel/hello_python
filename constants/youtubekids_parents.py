import time

from selenium import webdriver

driver = webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch(driver):
    driver.get("https://www.youtubekids.com/")
    driver.maximize_window()
    time.sleep(7)
launch(driver)

def choose_parents(driver,time):
    driver.find_element_by_id("parent-button").click()
    driver.find_element_by_id("next-button").click()
    time.sleep(2)
choose_parents(driver,time)

def hi_parents(driver,age):
    for x in range(1,5):
        driver.find_element_by_id("onboarding-age-gate-digit-"+str(x)).send_keys(age[x-1])
        time.sleep(1)
age=input("please enter your age parents")
hi_parents(driver,list(age))
time.sleep(2)

def submit(driver):
    driver.find_element_by_xpath("/html/body/ytk-app/div/ytk-kids-onboarding-flow-data-v2/div[3]/ytk-kids-onboarding-age-gate-renderer/div/div[5]/button").click()
submit(driver)

def video_page_to_text(driver):
    driver.execute_script("scrollTo(0,100)")
    driver.find_element_by_id("show-text-link").click()
    time.sleep(2)
    driver.execute_script("scrollTo(0,100)")
    driver.find_element_by_id("next-button").click()
video_page_to_text(driver)

