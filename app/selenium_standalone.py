import unittest
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SearchProducts(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platform'] = 'WINDOWS'
        # desired_caps['browserName'] = 'firefox'
        # desired_caps['browserName'] = 'chrome'
        desired_caps['browserName'] = 'internet explorer'
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # self.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME, options=options,)
        self.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_caps)
        self.driver.get('http://www.google.com/')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def testSearchByCategory(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys('motorolla')
        self.search_field.submit()
        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_elements_by_xpath method
        # products = self.driver.find_elements_by_xpath('//h2[@class=\'product-name\']/a')
        products = self.driver.find_elements_by_class_name('LC20lb DKV0Md')
        # check count of products shown in results
        # self.assertEqual(2, len(products))
        print('************S*************')
        print("No. of products : ", len(products))
        print('************E*************')

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

# https://www.selenium.dev/documentation/webdriver/remote_webdriver/

# java -Dwebdriver.chrome.driver="D:\Selenium\drivers\chromedriver.exe" -jar selenium-server-standalone-3.141.59.jar -role webdriver -browser "browserName=chrome,version=94.0.4606.81,maxinstance=1,platform=WINDOWS" -hubHost localhost -port 7777