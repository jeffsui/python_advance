from selenium import webdriver
edge_options = webdriver.EdgeOptions()
import time

driver = webdriver.Remote(command_executor='http://127.0.0.1:4444',options=edge_options)
driver.get('http://www.baidu.com')
time.sleep(2)
driver.quit()