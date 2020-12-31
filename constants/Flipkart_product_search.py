import time

from selenium import webdriver
from selenium.webdriver.common import keys

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def launch(driver,time):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    time.sleep(4)
launch(driver,time)

def search(driver,time):
    searching=driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    product = input("please enter a product you want to search")
    time.sleep(4)
    searching.send_keys(product)
    driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
search(driver,time)
time.sleep(4)


def wishlist(driver):
    driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/a[1]").click()
wishlist(driver)
time.sleep(2)

