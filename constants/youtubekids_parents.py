import time

from selenium import webdriver

driver = webdriver.Edge(executable_path="P:\Webdrivers\msedgedriver")

def launch(driver):
    driver.get("https://www.youtubekids.com/")
    driver.maximize_window()
    time.sleep(7)
launch(driver)

def choose_parents(driver,time):
    driver.find_element_by_id("parent-button").click()
    driver.find_element_by_id("next-button").click()
    time.sleep(2)
choose_parents(driver,time)

def hi_parents(driver,age):
    for x in range(1,5):
        driver.find_element_by_id("onboarding-age-gate-digit-"+str(x)).send_keys(age[x-1])
        time.sleep(1)
age=input("please enter your age parents")
hi_parents(driver,list(age))
time.sleep(2)

def submit(driver):
    driver.find_element_by_xpath("/html/body/ytk-app/div/ytk-kids-onboarding-flow-data-v2/div[3]/ytk-kids-onboarding-age-gate-renderer/div/div[5]/button").click()
submit(driver)

def video_page_to_text(driver):
    driver.execute_script("scrollTo(0,100)")
    driver.find_element_by_id("show-text-link").click()
    time.sleep(2)
    driver.execute_script("scrollTo(0,200)")
    driver.find_element_by_xpath("/html/body/ytk-app/div/ytk-kids-onboarding-flow-data-v2/div[3]/ytk-kids-sign-in-info-renderer/ytk-kids-flow-text-info-renderer/div/div[2]/div/div/button[2]").click()
video_page_to_text(driver)

def signin(driver):
    driver.find_element_by_id("skip-button").click()
signin(driver)

def notice_to_parent(driver):
    driver.execute_script("scrollTo(0,200)")
    driver.find_element_by_xpath("/html/body/ytk-app/div/ytk-kids-onboarding-flow-data-v2/div[3]/ytk-kids-onboarding-parental-notice-page-renderer/div/div[2]/div[2]/div/button").click()
notice_to_parent(driver)

def content_experience(driver):
    driver.find_element_by_xpath("/html/body/ytk-app/div/ytk-kids-onboarding-flow-data-v2/div[3]/ytk-kids-corpus-selection-renderer/div/div[2]/div/ytk-kids-age-selection-card-renderer[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/ytk-app/ytk-popup-container/paper-dialog/ytk-kids-corpus-selection-modal-renderer/div[1]/div[2]/div[2]/button[1]").click()
content_experience(driver)
time.sleep(5)

def search_turnon(driver):
    driver.execute_script("scrollTo(0,200)")
    driver.find_element_by_id("search-on-button").click()
    time.sleep(2)
    driver.execute_script("scrollTo(0,200)")
    driver.find_element_by_id("done-button").click()
search_turnon(driver)

def search_input(driver):
    driver.find_element_by_id("input").send_keys("Masha and the bear")
    driver.find_element_by_id("search-icon-container").click()
search_input(driver)
time.sleep(2)

def thumbnail(driver):
    driver.find_element_by_xpath("/html/body/ytk-app/div/ytk-search-response/div[2]/ytk-section-list-renderer/div[1]/ytk-item-section-renderer/div/ytk-compact-video-renderer[1]/a/div[1]/yt-img-shadow").click()
    time.sleep(2)
thumbnail(driver)
time.sleep(20)

def lock(driver):
    driver.find_element_by_xpath("/html/body/ytk-app/ytk-masthead/div/div[2]/div[2]/div[2]/paper-icon-button/iron-icon").click()
lock(driver)
time.sleep(2)

def problem(driver):
    lock_problem=driver.find_element_by_id("parental-gate-math-problem")
    print(lock_problem.text)
    multiply = input("please enter the answer of the multiplication")
    list(multiply)
    for x in range(1,3):
        driver.find_element_by_xpath("/html/body/ytk-app/ytk-parental-gate/div[2]/div[4]/input["+str(x)+"]").send_keys(multiply[x-1])

problem(driver)

