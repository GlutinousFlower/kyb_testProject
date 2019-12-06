import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import logging
import logging.config
import yaml
from appium import webdriver


#配置文件读取
with open('../config/kyb_caps.yaml','r',encoding='utf-8') as file:
    data=yaml.load(file,Loader=yaml.FullLoader)
#log配置文件读取
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


def appium_desired():
    desired_caps={}
    desired_caps['platformName']=data['platformName']

    #真机设备
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['udid']=data['udid']
    #desired_caps['deviceName']='vivo X21UD A'
    #desired_caps['udid']='34f5aa6e'

    #应用
    #对app存放路径进行拼接
    base_dir=os.path.dirname(os.path.dirname(__file__))
    app_path=os.path.join(base_dir,'app',data['app'])
    desired_caps['app']=app_path
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']

    desired_caps['noReset']=data['noReset']
    #中文输入设置
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    #配置可识别Toast
    desired_caps['automationName']=data['automationName']

    logging.info('start app....')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__=='__main__':

    appium_desired()