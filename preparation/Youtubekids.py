import time

from selenium import webdriver


class youtubekids():
    driver = webdriver.Edge("P:/Webdrivers/edgedriver.exe")

    def launch(driver):
        driver.get("https://www.youtubekids.com/")
        driver.maximize_window()

    launch(driver)

    time.sleep(3)

    def i_am_parent(driver):
        driver.find_element_by_id("parent-button").click()
        driver.find_element_by_id("next-button").click()

    i_am_parent(driver)
    time.sleep(4)

    def hi_parent(driver, year):

        for x in range(1, 4):
            driver.find_element_by_xpath(
                "/html/body/ytk-app/div/ytk-kids-onboarding-flow-data-v2/div[3]/ytk-kids-onboarding-age-gate-renderer/div/div[4]/input["+str(x)+"]").send_keys(
                year(x - 1))

    year =(input("please enter the year of birth"))
    hi_parent(driver,list(year))
