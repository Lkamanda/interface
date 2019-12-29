# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-29 15:10
@Author  : zhoujialin
@File    : test.py
'''

import unittest
from myFun import divide
from  common.configHttp import *
from ddt import data, ddt, unpack
from common.excal import readExcel
"""
1.接收数据，调用readExcal模块获取数据
2.处理请求 调用请求方法
        get post put delete
        - 封装
3.断言结果
    - assert 
    - 将接口返回的实际结果与预期结果进行对别      
"""
"""
1-导入目标模块或包
2-调用readExcel模块，获取测试数据
3-根据测试数据，调用相对用的接口方法，完成接口请求
4-获取实际结果
5-将实际结果和预期结果进行比对
6-接接口执行状态写入excal
"""

dt = readExcel()
test_data = dt.assembleData()
print(test_data[0])
test1 = test_data[0]
test2 = test_data[1]
test3 = test_data[2]

@ddt
class testCase(unittest.TestCase):

    @staticmethod
    def getData():
        data = readExcel()
        test_data = data.assembleData()
        return test_data


    @ddt
    @data(test1)
    @unpack
    def test1(self,*te):
        # id, url, name, method, param, expect
        print('test1')
        print(te[0])
        pass
        # self.assertEqual(4, divide(8,1))
    # #2
    # @ddt
    # @data(test1,test2,test3)
    # @unpack
    # def test2(self,te):
    #     print(te[0])
    #     # self.assertEqual(3, divide(8,2))
    

if __name__ == '__main__':
    unittest.main()



