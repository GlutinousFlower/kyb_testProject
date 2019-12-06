import sys
path='/Users/luping.xiao/PycharmProje'
sys.path.append(path)
#encoding=utf-8
import unittest
from BSTestRunner import BSTestRunner
import time
import logging
test_dir='../test_case'
report_dir='../reports'
#加载测试用例
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

#定义报告的文件格式
now=time.strftime('%Y-%m-%d %H:%M:%S')
report_name=report_dir+'/'+now+' test_report.html'

#运行用例并生成测试报告
with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title='kyb Test Report',description='kyb Android app Test Report')
    logging.info('start run test case.....')
    runner.run(discover)