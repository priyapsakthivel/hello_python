from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def date_Example(driver):
    driver.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
    driver.maximize_window()
    driver.execute_script("scrollTo(0,150)")
    driver.find_element_by_xpath("//*[@id='sandbox-container1']/div/input").click()
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/table/tbody/tr[3]/td[2]").click()
    date = driver.find_element_by_xpath("//*[@id='sandbox-container1']/div/input").text
    print(date)
date_Example(driver)