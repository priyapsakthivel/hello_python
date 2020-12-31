import time

from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\edgedriver.exe")
driver.get("https://www.seleniumeasy.com/test/bootstrap-dual-list-box-demo.html")
driver.maximize_window()
driver.execute_script("scrollTo(0,200)")
time.sleep(2)
driver.find_element_by_xpath("list-group-item").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/button[2]").click()

