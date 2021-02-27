import time

from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
a=input("please enter any number1")
b=input("please enter any number2")

def launching(driver):
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    driver.maximize_window()
launching(driver)
def popupclose(driver):
    driver.find_element_by_id("at-cv-lightbox-close").click()
    time.sleep(2)
    driver.execute_script("scrollTo(0,200)")
popupclose(driver)
def twoinputfield(driver,a,b):
    driver.find_element_by_id("sum1").send_keys(a)
    driver.find_element_by_id("sum2").send_keys(b)
    time.sleep(2)
