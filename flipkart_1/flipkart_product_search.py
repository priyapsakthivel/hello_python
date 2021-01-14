import time

from selenium import webdriver

from constants.path_constant import DRIVER_PATH, FLIPKART_URL

product_search=input("please enter a product you wanna search")
driver=webdriver.Edge(executable_path=DRIVER_PATH)
driver.get(FLIPKART_URL)
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys(product_search)
driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
time.sleep(10)
driver.quit()

