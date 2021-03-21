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
    driver.find_element_by_xpath("/html/body/ytk-app/div/ytk-kids-onboarding-flow-data-v2/div[3]/ytk-kids-onboarding-age-gate-renderer/div/div[4]").send_keys("1997")
hi_parent(driver)