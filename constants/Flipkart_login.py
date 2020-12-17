import time

from selenium import webdriver
driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def flipkart_login(driver):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys("9042003857")
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
flipkart_login(driver)
time.sleep(2)
def otp_length(driver,otp):
    for x in range(1,7):
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/div/form/div/div["+str(x)+"]/input").send_keys(otp(x-1))

otp = input("please enter otp")
otp_length(driver,list(otp))

