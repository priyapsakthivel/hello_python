#
import time

from selenium import webdriver
searching= input("please enter a program you with to search")
driver = webdriver.Edge(executable_path='P:\Webdrivers\msedgedriver')


def driverlaunch():
    driver.get("https://www.hotstar.com/in")
    driver.maximize_window()
driverlaunch()
time.sleep(5)


def search():
    driver.find_element_by_id("searchField").send_keys(searching)
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[1]/div/div[2]/div/div[4]/div[2]/div[3]/article/a").click()
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/div[1]/div[1]/a").click()
search()

