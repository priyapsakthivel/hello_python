import time


def selenium_easy_login(driver):
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    time.sleep(2)
    driver.find_element_by_id("at-cv-lightbox-close").click()
    driver.maximize_window()
    driver.execute_script("scrollTo(0,100)")
    time.sleep(2)

