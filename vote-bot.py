from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"


driver = webdriver.Chrome(PATH)

# Insert the poll link here
driver.get("https://fast-poll.com/poll/56e76cd9")

time.sleep(1)

search = driver.find_element_by_id("gdpr-cookie-accept")
search.send_keys(Keys.RETURN)

time.sleep(1)

search = driver.find_element_by_class_name("vote-inner-label").click()
search = driver.find_element_by_xpath('//*[@title="Submit your vote"]').click()

driver.quit()
    