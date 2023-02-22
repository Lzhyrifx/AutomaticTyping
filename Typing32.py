import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()  # Firefox驱动
driver.maximize_window()  # 网页最大化
time.sleep(10)
driver.get('')  # 跳转到指定网页
time.sleep(30)
driver.find_element(by=By.ID, value='Button2').click()
while True:
    text = driver.find_element(by=By.ID, value='TextWord').text
    driver.find_element(by=By.ID, value='InputWord').send_keys(text)
