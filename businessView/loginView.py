import logging
from common.common_fun import Common
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginView(Common):
    #登录界面元素
    username_ele=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_ele=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')

    #个人中心下线元素
    commitBtn=(By.ID,'com.tal.kaoyan:id/tip_commit')

    #检测用户是否登录
    button_myself=(By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    usercenter_username=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    #退出登录Btn
    settingBtn=(By.ID,'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    logoutBtn=(By.ID,'com.tal.kaoyan:id/setting_logout_text')
    tip_commit=(By.ID,'com.tal.kaoyan:id/tip_commit')

    def login_action(self,username,password):
        self.check_cancleBtn()
        self.check_skipBtn()

        logging.info('=======login========')
        logging.info('input username:%s'%username)
        self.driver.find_element(*self.username_ele).clear()
        self.driver.find_element(*self.username_ele).send_keys(username)

        logging.info('input password:%s'%password)
        self.driver.find_element(*self.password_ele).send_keys(password)

        logging.info('click loginBtn.')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished.')


    def check_account_alert(self):
        '''检测账户登录厚是否有账户下线通知'''
        logging.info('========check_account_alert=========')
        try:
            element=self.driver.find_element(*self.commitBtn)
        except NoSuchElementException:
            pass
        else:
            logging.info('click commitBtn~')
            element.click()


    def check_loginStatus(self):
        logging.info('========check_loginStatus=======')
        self.check_market_ad()
        self.check_account_alert()
        try:
           self.driver.find_element(*self.button_myself).click()
           element=self.driver.find_element(*self.usercenter_username)
        except NoSuchElementException:
            logging.error('login fail~')
            self.getScreenshot('loginFail')
            return False
        else:
            logging.info('login success~')
            self.logout_action()
            return True


    def logout_action(self):
        '''退出登录操作'''
        logging.info('=========logout action=========')
        self.driver.find_element(*self.settingBtn).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()


#
# driver=appium_desired()
# l=LoginView(driver)
# l.login_action('自学网2018','zxw289218')
# l.check_loginStatus()