from selenium import webdriver

driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def dropdown():
    driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
    driver.maximize_window()
    driver.execute_script("scrollTo(0,200)")
    drop=driver.find_element_by_id("select-demo").text
    drop.select_by_visible_text('Sunday')
dropdown()