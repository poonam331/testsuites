from behave import *
from selenium import webdriver

@given('We launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path='D:\Selenium\drivers\chromedriver.exe')
    
@when('we open orange hrm Homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')

@when('So Enter username "{user}"  and password "{pwd}"')
def enterLoginDetails(context, user, pwd):
    context.driver.find_element_by_id('txtUsername').send_keys(user)
    context.driver.find_element_by_id('txtPassword').send_keys(pwd)

@when('Now Click on login button')
def clickLogin(context):
    context.driver.find_element_by_id('btnLogin').click()


@then('User must successfully login to the Dashboard page and see the header Dashboard')
def viewDashboard(context):
    try :
        text = context.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').text
    except:
        context.driver.close()
        assert False,"Test Failed"
    if text == 'Dashboard':
        context.driver.close()
        assert True, "Test Passed"
    
    
