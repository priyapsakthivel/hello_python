import time

from selenium import webdriver

element=input("please enter any one of the following Green/Orange/Red/All colour you wanna choose")
driver=webdriver.Edge(executable_path="P:/Webdrivers/edgedriver.exe")
driver.get("https://www.seleniumeasy.com/test/table-records-filter-demo.html")
driver.maximize_window()
driver.execute_script("ScrollTo(0,200)")


# for i in range(element):
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[1]").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[1]").text



