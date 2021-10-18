from behave import *
from selenium import webdriver
from allure_behave.hooks import allure_report

allure_report("D:\Selenium\behave_example\reports")

@given('User launch browser')
def step_impl(context):
    print('STEP 1: Given User launch browser')
    assert True,"Test Passed"

@when('User open application')
def step_impl(context):
    print('STEP 2: When User open application')
    assert True,"Test Passed"

@when('User Enter valid username and password')
def step_impl(context):
    print('STEP 3: When User Enter valid username and password')
    assert True,"Test Passed"

@when('User click on login button')
def step_impl(context):
    print('STEP 4: When User click on login button')
    assert True,"Test Passed"

@then('User must be able to login to Dashboard page')
def step_impl(context):
    print('STEP 5: Then User must be able to login to Dashboard page')
    assert True,"Test Passed"

@when('navigate to search page')
def step_impl(context):
    print('STEP 6: When navigate to search page')
    assert True,"Test Passed"

@then('search page should display')
def step_impl(context):
    print('STEP 7: Then search page should display')
    assert True,"Test Passed"

@when('navigate to advanced search page')
def step_impl(context):
    print('STEP 8: When navigate to advanced search page')
    assert True,"Test Passed"

@then('advanced search page should display')
def step_impl(context):
    print('STEP 9: Then advanced search page should display')
    assert True,"Test Passed"

#Commant to generate the allure report

# D:\Selenium\behave_example>
# behave -f allure_behave.formatter:AllureFormatter -o reports/ features/backgroundorangehrm.feature
#allure serve reports/

# C:\Program Files\Common Files\Oracle\Java\javapath;C:\ProgramData\Oracle\Java\javapath;C:\Program Files\PC Connectivity Solution\;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files\Toshiba\Bluetooth Toshiba Stack\sys\;C:\Program Files\Java\jre1.8.0_131\bin;C:\Projects\python\Scripts;C:\Projects\python\Lib\site-packages;C:\Projects\python;C:\Program Files\jenkins;C:\Program Files\Javanew\bin