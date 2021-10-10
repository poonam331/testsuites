import unittest

class LoginTest(unittest.TestCase):
    def test_LoginByEmail(self):
        print('This is login by test')
        self.assertTrue(True)
    
    def test_LoginByfacebook(self):
        print('This is login by Facebook')
        self.assertTrue(True)

    def test_LoginBytwitter(self):
        print('This is login by Twitter')
        self.assertTrue(True)