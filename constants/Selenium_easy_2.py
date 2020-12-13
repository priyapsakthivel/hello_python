from selenium import webdriver

driver = webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
number1 = input("please enter number 1")
number2 = input("please enter number 2")


def launch(driver):
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    driver.maximize_window()
    driver.execute_script("scrollTo(0,600)")
    driver.find_element_by_id("at-cv-lightbox-close").click()


def sumimg(driver):
    driver.find_element_by_id("sum1").send_keys(number1)
    driver.find_element_by_id("sum2").send_keys(number2)
    driver.find_element_by_xpath("//*[@id='gettotal']/button").click()


launch(driver)
sumimg(driver)
