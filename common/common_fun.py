from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time
import os
import csv

class Common(BaseView):
    cancelBtn=(By.ID,'android:id/button2')
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')

    #登录之后出现广告弹窗，关闭Btn
    wemedia_cacel=(By.ID,'com.tal.kaoyan:id/view_wemedia_cancel')


    def check_cancleBtn(self):
        logging.info('=======check cancleBtn=======')
        try:
            cancelBtn=self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('========no cancleBtn=======')
        else:
            logging.info('click cancelBtn~')
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info('=======check skipBtn=======')
        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('========no skipBtn=======')
        else:
            logging.info('click skipBtn~')
            skipBtn.click()

    def get_screenSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft~')
        l=self.get_screenSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def swipeUp(self):
        logging.info('swipeUp~')
        l=self.get_screenSize()
        x1 = int(l[1] * 0.5)
        y1 = int(l[0] * 0.9)
        y2 = int(l[0] * 0.1)
        self.swipe(x1,y1,x1,y2,1000)


    def getTime(self):
        self.now=time.strftime('%Y-%m-%d %H:%M:%S')
        return self.now

    def getScreenshot(self,moudle):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png'%(moudle,time)
        logging.info('get %s screenshot'%moudle)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        '''检测登录或注册之后对界面浮窗广告'''
        logging.info('========check_market_ad=======')
        try:
            element=self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging('close market ad~')
            element.click()


    def get_csv_data(self,csv_file,line):
        logging.info('========get csv data========')
        with open(csv_file,'r',encoding='utf-8')as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row







# driver=appium_desired()
# com=Common(driver)
# com.check_cancleBtn()
# com.check_skipBtn()
# com.swipeLeft()
# com.getScreenshot('swipe1')

# if __name__=='__main__':
#     # list=['这','是','一个','测试','数据']
#     # for i in range(len(list)):
#         # print(i,list[i])
#
#     # for index,item in enumerate(list):
#     #     print(index,item)
#     def get_csv_data(csv_file,line):
#         with open(csv_file,'r',encoding='utf-8')as file:
#             reader=csv.reader(file)
#             for index,row in enumerate(reader,1):
#                 if index==line:
#                     return row
#
#     csv_file='../data/account.csv'
#     data=get_csv_data(csv_file,1)
#     print(data)