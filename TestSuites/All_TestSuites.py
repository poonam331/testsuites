import sys
sys.path.append("D://Selenium")
import unittest
from package1.TC_loginTest import LoginTest
from package1.TC_signUpTest import SignupTest
from package1.TC_title_check import CheckTitle
from package2.TC_paymentTest import PaymentTest
from package2.TC_paymentReturnsTest import PaymentReturnTest
# import HtmlTestRunner
from xmlrunner import xmlrunner


#Get all the test methods from LoginTest, SignupTest, PaymentTest, PaymentReturnTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)
tc5 = unittest.TestLoader().loadTestsFromTestCase(CheckTitle)

#Creating Test Suites
# sanityTestSuite = unittest.TestSuite([tc1, tc2])
# functionalTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])

# unittest.TextTestRunner(verbosity=2).run(masterTestSuite)

# if __name__ == '__main__':
#     unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))

xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(masterTestSuite)


# C:\Program Files\Common Files\Oracle\Java\javapath;C:\ProgramData\Oracle\Java\javapath;C:\Program Files\PC Connectivity Solution\;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files\Toshiba\Bluetooth Toshiba Stack\sys\;C:\Projects\python\Scripts;C:\Projects\python\Lib\site-packages;C:\Projects\python;C:\Program Files\jenkins

# C:\Program Files\Java\jre1.8.0_131\bin;
