import time
from selenium import webdriver
driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
driver.get("https://10fastfingers.com/typing-test/english")
driver.maximize_window()
time.sleep(5)
for x in range(1,360):
    word=driver.find_element_by_xpath("//*[@id='row1']/span["+ str(x)+"]")
    driver.find_element_by_id("inputfield").send_keys(word+" ")


