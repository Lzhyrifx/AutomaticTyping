import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(10)
driver.get('http://10.189.240.90/')
time.sleep(30)
driver.find_element(by=By.ID, value='Button2').click()
while True:
    text = driver.find_element(by=By.ID, value='TextWord').text
    driver.find_element(by=By.ID, value='InputWord').send_keys(text)
