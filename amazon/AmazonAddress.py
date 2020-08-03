import time

from selenium import webdriver

emailid = input("please enter your emailid")
password = input("please enter your password")

driver=webdriver.Edge(executable_path="P:\Webdrivers\edgedriver.exe")
driver.get("https://www.amazon.in/")
time.sleep(5)
driver.find_element_by_xpath("\\*[@id='nav-link-accountList']").click()
driver.maximize_window()
time.sleep(5)
driver.find_element_by_id("ap_email").sendkeys(emailid)
driver.find_element_by_id("continue").click()
time.sleep(5)
driver.find_element_by_id("ap_password").send_keys(password)
driver.find_element_by_id("signInSubmit").click()
time.sleep(5)
driver.find_element_by_id("nav-hamburger-menu").click()
driver.find_element_by_id("hmenu-customer-profile-link").click()
driver.find_element_by_xpath("//*[@id='a-page']/div[2]/div/div[3]/div[1]/a").click()
driver.find_element_by_id("ya-myab-address-add-link").click()