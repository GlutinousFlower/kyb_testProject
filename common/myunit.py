import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from common.desired_caps import appium_desired
# from businessView.registerView import RegisterView
import random
import logging
from time import sleep

class StartEnd(unittest.TestCase):

    driver=appium_desired()

    def SetUp(self):
        logging.info('===========SetUp=========')
        # self.driver=appium_desired()

    def TearDown(self):
        logging.info('=========TearDown========')
        sleep(5)
        self.driver.close_app()


# if __name__=='__main__':
#     unittest.main()
