import time

from selenium import webdriver

driver= webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def single_input_field(driver):
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    driver.maximize_window()
    driver.execute_script("scrollTo(0,100)")
    driver.find_element_by_id("user-message").send_keys("selenium")
    time.sleep(2)
    driver.find_element_by_id("at-cv-lightbox-close").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='get-input']/button").click()
    time.sleep(8)
    show =driver.find_element_by_id("user-message")
    print(show.text)
    driver.get_screenshot_as_file (" C:/Users/Mohan/Pictures/Screenshots "+ show + ".png")
single_input_field(driver)