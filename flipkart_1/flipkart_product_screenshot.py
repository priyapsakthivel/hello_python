import time

from selenium import webdriver

from constants.flipkart_product_search_method import flipkart_search
from constants.path_constant import FLIPKART_URL

search = input("please enter a product you wanna search")
driver=webdriver.Edge(executable_path="P:/Webdrivers/edgedriver.exe")
flipkart_search(FLIPKART_URL,search,driver)
time.sleep(2)
driver.get_screenshot_as_file("P:/screenshot/"+search+".png")