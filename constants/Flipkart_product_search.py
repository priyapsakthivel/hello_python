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
    searching.send_keys(keys.ENTER)
search(driver,time)
