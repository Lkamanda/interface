# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-29 17:59
@Author  : zhoujialin
@File    : writeExcal.py
'''
import xlrd
from xlutils.copy import copy
import time

class writeExcal(object):

    def __init__(self, status):
        self.path = r'./testData/data_demo.xls'
        self.status = status
        self.length = len(status)

    def write(self):
        rb = xlrd.open_workbook(self.path)
        wb = copy(rb)
        ws = wb.get_sheet(2)
        for i in range(self.length):
            ws.write(i+1,3, self.status[i])
        path = self.path
        wb.save(path)

    def get_SavePath(self):
        str_time = time.strftime('%Y-%m-%d %H-%M-%S')
        path = '../testData/data_{}.xls'.format(str_time)
        return path


    def close(self):
        pass


if __name__ == '__main__':
    r = [1,2,4]
    a = writeExcal(r)
    a.write()