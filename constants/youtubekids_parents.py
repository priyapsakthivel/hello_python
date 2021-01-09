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
    driver.execute_script("scrollTo(0,200)")
    driver.find_element_by_xpath("/html/body/ytk-app/div/ytk-kids-onboarding-flow-data-v2/div[3]/ytk-kids-sign-in-info-renderer/ytk-kids-flow-text-info-renderer/div/div[2]/div/div/button[2]").click()
video_page_to_text(driver)

def signin(driver):
    driver.find_element_by_id("skip-button").click()
signin(driver)

def notice_to_parent(driver):
    driver.execute_script("scrollTo(0,200)")
    driver.find_element_by_xpath("/html/body/ytk-app/div/ytk-kids-onboarding-flow-data-v2/div[3]/ytk-kids-onboarding-parental-notice-page-renderer/div/div[2]/div[2]/div/button").click()
notice_to_parent(driver)

def content_experience(driver):
    driver.find_element_by_xpath("/html/body/ytk-app/div/ytk-kids-onboarding-flow-data-v2/div[3]/ytk-kids-corpus-selection-renderer/div/div[2]/div/ytk-kids-age-selection-card-renderer[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/ytk-app/ytk-popup-container/paper-dialog/ytk-kids-corpus-selection-modal-renderer/div[1]/div[2]/div[2]/button[1]").click()
content_experience(driver)
time.sleep(5)

def search_turnon(driver):
    driver.execute_script("scrollTo(0,200)")
    driver.find_element_by_id("search-on-button").click()
    time.sleep(2)
    driver.execute_script("scrollTo(0,200)")
    driver.find_element_by_xpath("done-button")
search_turnon(driver)

