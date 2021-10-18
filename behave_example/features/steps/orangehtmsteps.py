# from behave import given, when, then
from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):        
    context.driver = webdriver.Chrome(executable_path='D:\Selenium\drivers\chromedriver.exe')

@when('open orange hrm homepage')
def openHomePage(context):    
    context.driver.get('https://opensource-demo.orangehrmlive.com/')

@then('verify that logo presence on page')
def verifyLogo(context):    
    status = context.driver.find_element_by_xpath('//*[@id="divLogo"]/img').is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):    
    context.driver.close()

