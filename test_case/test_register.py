from common.myunit import StartEnd
from businessView.registerView import RegisterView
from common.desired_caps import appium_desired
import logging
import random
import unittest

class RegisterTest(StartEnd):
    def test_user_register(self):
        logging.info('=========test user register==========')
        r=RegisterView(appium_desired())
        username = 'zxw2018' + 'xlp' + str(random.randint(1000, 9000))
        password = 'zxw' + str(random.randint(1000, 9000))
        email = '51zxw' + str(random.randint(1000, 9000)) + '@163.com'

        self.assertTrue(r.register_action(username,password,email))


if __name__=='__main__':
    unittest.main()