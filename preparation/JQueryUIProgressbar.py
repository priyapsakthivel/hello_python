import time

from selenium import webdriver

driver= webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver.exe")
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
driver.maximize_window()
driver.find_element_by_id("downloadButton").click()
time.sleep(200)
download=driver.find_element_by_xpath("//*[@id='dialog']/div[1]").text
print(download)
driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/button").click()

