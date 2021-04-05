import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

program= input ("please enter a program you wanna watch ")
driver=webdriver.Edge(executable_path="P:/Webdrivers/edgedriver.exe")
driver.get("https://www.hotstar.com/in")
driver.maximize_window()
driver.find_element_by_id("searchField").send_keys(program)
driver.find_element_by_id("searchField").send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div/article/a/div[2]").click()
time.sleep(50)
#driver.quit()


