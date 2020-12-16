from selenium import webdriver
driver=webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")
def flipkart_login(driver):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys("9042003857")
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
flipkart_login(driver)