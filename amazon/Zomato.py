import time

from selenium import webdriver

driver= webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def launch(driver):
    driver.get("https://www.zomato.com/india")
    driver.maximize_window()
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/header/nav/ul[2]/li[2]/a").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/section[2]/section/div[1]/div/input").send_keys("9080442336")
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/section[2]/section/button").click()
launch(driver)

def otp(driver):
    for x in range(1,7):
     driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/section[2]/section/div/div/div/input["+str(x)+"]").send_keys(x-1)
otp(driver)

