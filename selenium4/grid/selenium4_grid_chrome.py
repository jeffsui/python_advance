from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
import time

driver = webdriver.Remote(command_executor='http://127.0.0.1:4444',options=chrome_options)
driver.get('http://www.baidu.com')
time.sleep(2)
driver.quit()