import time

from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def launching(driver):
    driver.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
    driver.maximize_window()
launching(driver)
def bootstrap(driver):
    driver.execute_script("scrollTo(0,200)")
    driver.find_element_by_xpath("//*[@id='sandbox-container1']/div/span").click()
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/table/tfoot/tr[1]/th").click()
    time.sleep(12)
    driver.find_element_by_xpath("//*[@id='sandbox-container1']/div/span").click()
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/table/tfoot/tr[2]/th").click()
bootstrap(driver)

