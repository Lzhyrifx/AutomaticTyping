from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service("Z:\Project\Python\Python39\msedgedriver.exe"))
driver.maximize_window()
driver.get('')
driver.find_element(by=By.XPATH, value='//*[@id="dom-indexTabs"]/li[2]/a').click()
driver.find_element(by=By.XPATH, value='//*[@id="dom-indexPnls"]/div[2]/form/div[3]/button').click()
for z in range(10086):
    text = driver.find_element(by=By.ID, value=f'box_{z}').text
    driver.find_element(by=By.XPATH, value='''//*[@id="box_''' + str(z) + '''"]/input[2]''').send_keys(text, Keys.SPACE)
