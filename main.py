# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-29 10:44
@Author  : zhoujialin
@File    : main.py
'''

"""
1。找到所有的测试用例子
2运行测试用列
3。生成报告
4。调用邮件木哦快

"""
from testReport.HTMLTestRunner import HTMLTestRunner
import unittest
import os
import time
gPath = os.path.dirname(__file__)
class Runner(object):

    def getSuite(self):
        # start_dir = 'C:/Users/zhoujialin/PycharmProjects/interface'+
        start_dir = gPath + '/testCase'
        # discover = unittest.defaultTestLoader().discover()
        suite = unittest.TestLoader().discover(
            start_dir = start_dir,
            pattern = 'test*.py',
            top_level_dir = None
        )
        return suite

    def run(self):
        now_time = time.strftime('%Y-%m-%d %H-%M-%S')
        report_file = gPath+ '/testReport/ %s Test Report.html' % now_time
        fp = open(report_file, 'wb')
        runner = HTMLTestRunner(
            stream = fp,
            title='test report',
            description='version-2'
        )
        suite = self.getSuite()
        runner.run(suite)

    def clearReport(self):
        # 获取目标目录所有文件
        # 按照 时间 进行筛选
        # 删除 筛选出来不符合规则的的文件
        pass


if __name__ == '__main__':
    r = Runner()
    r.run()

# 发送邮件
# 定期清理报告文件
# 缺少logging模块
# dev
#  vip test2








