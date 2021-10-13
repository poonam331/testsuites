import unittest
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_caps = {}
desired_caps['platform'] = 'WINDOWS'
desired_caps['browserName'] = 'internet explorer'
# driver = webdriver.Ie('D:\\Selenium\\app\\IEDriverServer.exe')
driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_caps)

driver.get('http://www.google.com/')
driver.implicitly_wait(30)
driver.maximize_window()
driver.quit()

 
# https://www.selenium.dev/documentation/webdriver/remote_webdriver/