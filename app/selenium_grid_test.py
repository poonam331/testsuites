import sys
import unittest
from selenium import webdriver

class SearchProducts(unittest.TestCase):
    PLATFORM = 'WINDOWS'
    # BROWSER = 'internet explorer'
    BROWSER = 'chrome'

    def setUp(self):
        desired_caps = {}
        desired_caps['platform'] = self.PLATFORM                
        desired_caps['browserName'] = self.BROWSER
        # desired_caps['browserName'] = 'firefox'
        # desired_caps['browserName'] = 'internet explorer'
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
    if len(sys.argv) > 1:
        SearchProducts.BROWSER = sys.argv.pop()
        SearchProducts.PLATFORM = sys.argv.pop()
        unittest.main(verbosity=2)
