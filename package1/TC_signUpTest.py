import unittest

class SignupTest(unittest.TestCase):
    def test_SignupByEmail(self):
        print('This is Signup by test')
        self.assertTrue(True)
    
    def test_SignupByfacebook(self):
        print('This is Signup by Facebook')
        self.assertTrue(True)

    def test_SignupBytwitter(self):
        print('This is Signup by Twitter')
        self.assertTrue(True)