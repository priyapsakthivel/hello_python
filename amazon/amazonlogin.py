import time

from selenium import webdriver

emailid=input("please  enter your valid email address")
password=input("please enter your password")

def amazonloginpage(emailid,password):
    driver=webdriver.Edge(executable_path="P:\Webdrivers\edgedriver.exe")
    driver.get("https://www.amazon.com/")
    driver.find_element_by_id("nav-signin-tooltip").click()
    time.sleep(2)

    driver.find_element_by_id("ap_email").send_keys(emailid)
    driver.find_element_by_id("continue").click()
    time.sleep(2)
    driver.find_element_by_id("ap_password").send_keys(password)
    driver.find_element_by_xpath("//*[@id='authportal-main-section']/div[2]/div/div/div/form/div/div[2]/div/div/label/div/label/input").click()
    driver.find_element_by_id("signInSubmit").click()

amazonloginpage(emailid,password)



