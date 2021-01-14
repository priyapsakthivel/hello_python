from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def launch(driver):
    driver.get("https://www.covid19india.org/")
    driver.maximize_window()
launch(driver)

def search(driver):
    search_box=input("Search your district or state")
    search_input= driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]/div[1]/div[1]/div[2]")
    search_input.send_keys(search_box)
    search_input.send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//*[@id='root']/div/div[3]").click()   #to stop extra suggetion


search(driver)