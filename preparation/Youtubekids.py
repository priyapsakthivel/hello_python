from selenium import webdriver
driver=webdriver.Edge("P:/Webdrivers/edgedriver.exe")
def launch(driver):
    driver.get("https://www.youtubekids.com/")
    driver.maximize_window()
launch(driver)
def i_am_parent(driver):
    driver.find_element_by_id("parent-button").click()
    driver.
i_am_parent(driver)
