from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://google.com')
browser.find_element(By.CLASS_NAME,'gLFyf').send_keys('python')
browser.find_element(By.CLASS_NAME,'QCzoEc').click()

time.sleep(60)