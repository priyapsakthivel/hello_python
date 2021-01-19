import time

from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def launch(driver):
    driver.get("https://www.covid19india.org/")
    driver.maximize_window()
launch(driver)

def search(driver):
    search_box=input("Search your district or state")
    search_input= driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[1]/div[1]/div[2]/input")
    search_input.send_keys(search_box+" ")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[1]/div[1]/div[3]/a/div").click()
    time.sleep(2)
    confirmed=driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[2]/div[1]/div[2]").text
    print("confirmed cases :" + confirmed)
    time.sleep(2)
search(driver)