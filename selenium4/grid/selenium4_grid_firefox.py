from selenium import webdriver

import time
firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444',options=firefox_options)
driver.get('http://www.baidu.com')
time.sleep(2)
driver.quit()