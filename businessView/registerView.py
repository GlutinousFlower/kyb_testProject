import logging
from common.desired_caps import appium_desired
from common.common_fun import Common
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
import time

class RegisterView(Common):
    #登录注册页面注册按钮
    register_text=(By.ID,'com.tal.kaoyan:id/login_register_text')
    #头像设置相关元素
    userheader=(By.ID,'com.tal.kaoyan:id/activity_register_userheader')
    user_image=(By.ID,'com.tal.kaoyan:id/item_image')
    saveBtn=(By.ID,'com.tal.kaoyan:id/save')

    #用户名密码,邮箱输入相关元素
    register_username=(By.ID,'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password=(By.ID,'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email=(By.ID,'com.tal.kaoyan:id/activity_register_email_edittext')
    registerBtn=(By.ID,'com.tal.kaoyan:id/activity_register_register_btn')

    #完善资料页面元素
      #选择目标院校
    perfectinfomation_school=(By.ID,'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    cities_chose=(By.ID,'com.tal.kaoyan:id/more_forum_title')
    university_items=(By.ID,'com.tal.kaoyan:id/university_search_item_name')
        #选择目标专业
    perfectinfomation_major=(By.ID,'com.tal.kaoyan:id/activity_perfectinfomation_major')
    marjorsubject_xueshu=(By.ID,'com.tal.kaoyan:id/activity_marjorsubject_xueshu')
    major_subject_titles=(By.ID,'com.tal.kaoyan:id/major_subject_title')
    major_group_titles=(By.ID,'com.tal.kaoyan:id/major_group_title')
    major_iterm_names=(By.ID,'com.tal.kaoyan:id/major_search_item_name')

    #进入考研帮
    goBtn=(By.ID,'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    #检测是否登录成功·
    button_myself=(By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    usercenter_username=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    def register_action(self,register_name,register_pwd,register_email):
        self.check_cancleBtn()
        self.check_skipBtn()


        logging.info('========register_action=========')
        self.driver.find_element(*self.register_text).click()


        #设置用户头像
        logging.info('set userHeader~')
        self.driver.find_element(*self.userheader).click()
        # self.driver.element_wait(12,self.user_image)
        time.sleep(15) #待改进，封装元素等待方法
        self.driver.find_elements(*self.user_image)[9].click()
        self.driver.find_element(*self.saveBtn).click()


        #输入用户名密码
        logging.info('register username is %s'%register_name)
        self.driver.find_element(*self.register_username).send_keys(register_name)
        logging.info('register password is %s' %register_pwd)
        self.driver.find_element(*self.register_password).send_keys(register_pwd)
        logging.info('register email is %s' %register_email)
        self.driver.find_element(*self.register_email).send_keys(register_email)
        logging.info('click registerBtn')
        self.driver.find_element(*self.registerBtn).click()

        #判断是否进入完善资料页面
        try:
            self.driver.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            logging.info('register failed~')
            self.getScreenshot('registerFail')
            return False
        else:
            self.add_register_info()
            if self.check_register_status():
                return True
            else:
                return False


        #添加注册信息
    def add_register_info(self):
        logging.info('=========add register info=======')
        logging.info('select school.....')
        self.driver.find_element(*self.perfectinfomation_school).click()
        self.driver.find_elements(*self.cities_chose)[1].click()
        self.driver.find_elements(*self.university_items)[1].click()
        logging.info('select major......')
        self.driver.find_element(*self.perfectinfomation_major).click()
        self.driver.find_element(*self.marjorsubject_xueshu).click()
        self.driver.find_element(*self.major_subject_titles)[1].click()
        self.driver.find_elements(*self.major_group_titles)[2].click()
        self.driver.find_elements(*self.major_iterm_names)[0].click()
        logging.info('click goBtn......')
        self.driver.find_element(*self.goBtn).click()
        logging.info('===========register finished=========')



    def check_register_status(self):
        logging.info('=========check register status========')
        self.check_market_ad()
        try:
           self.driver.find_element(*self.button_myself).click()
           element=self.driver.find_element(*self.usercenter_username)
        except NoSuchElementException:
            logging.error('register fail~')
            self.getScreenshot('registerFail')
            return False
        else:
            logging.info('register success~')
            return True




# driver=appium_desired()
# r=RegisterView(driver)
# username='zxw2018'+'xlp'+str(random.randint(1000,9000))
# password='zxw'+str(random.randint(1000,9000))
# email='51zxw'+str(random.randint(1000,9000))+'@163.com'
# r.register_action(username,password,email)
