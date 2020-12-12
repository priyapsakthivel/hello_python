#
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

searching= input("please enter a program you with to search")
driver = webdriver.Edge(executable_path='P:\Webdrivers\msedgedriver')
def driverlaunch(driver):
    driver.get("https://www.hotstar.com/in")
    driver.maximize_window()
driverlaunch(driver)
time.sleep(2)

def search(driver):
    searchfor=driver.find_element_by_id("searchField")
    searchfor.send_keys(searching)
    searchfor.send_keys(Keys.ENTER)
search(driver)
time.sleep(2)

def progaramSearch(driver):
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div/div/article/a").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,300)")
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div[6]/div/div/div/article/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/a").click()
progaramSearch(driver)




