# hotstar_login
import time

from selenium import webdriver

number = input("please enter your phone number")
driver = webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")


def launch(driver):
    driver.get("https://www.hotstar.com/in")
    driver.maximize_window()
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[1]/div/div[2]/div/div[5]").click()


def login_phonenumber(driver):
    driver.find_element_by_id("phoneNo").send_keys(number)
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='app']/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/button").click()


def otp(driver, otp_number):
    for x in range(1, 5):
        driver.find_element_by_xpath(
            "//*[@id='app']/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/input[" +  str(x)+ "]").send_keys(otp_number[x-1])
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/button").click()

launch(driver)
time.sleep(2)
login_phonenumber(driver)
otp_number = input("please enter your otp")
otp(driver, list(otp_number))
