import time

from selenium import webdriver

driver= webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def launch(driver):
    driver.get("https://www.zomato.com/akola/restaurants?context=delivery")
    driver.maximize_window()
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/header/nav/ul[2]/li[2]/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/section[2]/section/div[1]/div/input").send_keys("9080444947")
    time.sleep(2)
launch(driver)