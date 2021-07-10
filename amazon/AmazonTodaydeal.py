import time

from selenium import webdriver

# email_id = input("please enter your emailid")
# password = input("please enter your password")

driver=webdriver.Edge(executable_path="P:\Webdrivers\edgedriver.exe")
driver.get("https://www.amazon.in/")
time.sleep(5)
driver.find_element_by_id("nav-link-accountList").click()
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[3]/div[2]/div/a[3]").click()

