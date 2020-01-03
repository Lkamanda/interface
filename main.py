# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-29 10:44
@Author  : zhoujialin
@File    : main.py
'''
from testReport.HTMLTestRunner import HTMLTestRunner
import unittest
import os
import time
gPath = os.path.dirname(__file__)
class Runner(object):

    def getSuite(self):
        # start_dir = 'C:/Users/zhoujialin/PycharmProjects/interface'+
        start_dir = gPath + '/testCase'
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

if __name__ == '__main__':
    r = Runner()
    r.run()








