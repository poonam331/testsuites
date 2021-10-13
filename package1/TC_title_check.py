import unittest
from selenium import webdriver
import time
class CheckTitle(unittest.TestCase):
    def test_Title(self):
        self.driver = webdriver.Chrome(executable_path='D:\Selenium\drivers\chromedriver.exe')
        self.driver.get("https://www.google.com/")
        print('Title is : ', self.driver.title)        
        self.assertTrue(self.driver.title, "Google")
        time.sleep(5)
        # self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=3)