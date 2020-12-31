import time

from selenium import webdriver

from selenium_easy.Selenium_easy_login import selenium_easy_login
input_text=input("please enter a message you wanna display")
driver=webdriver.Edge(executable_path="P:/Webdrivers/edgedriver.exe")
selenium_easy_login(driver)
time.sleep(2)
driver.find_element_by_id("user-message").send_keys(input_text)
driver.find_element_by_xpath("//*[@id='get-input']/button").click()
time.sleep(2)
message_displayed=driver.find_element_by_id("display").text
time.sleep(2)
if(str(message_displayed)==str(input_text)):
    print(message_displayed +"and"+"your message is same")
else:
    print("message is not the same")