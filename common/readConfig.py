# -*- coding: utf-8 -*-
'''
@Time    : 2020-01-04 15:26
@Author  : zhoujialin
@File    : readConfig.py
'''
"""
导包
创建对象
"""

import configparser


configPath = r'../config.ini'
class readConfig():

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='utf-8-sig')

    def getConfig_email(self, name):
        name = self.cf.get('email', name)
        return name

if __name__ == '__main__':
    readC = readConfig()
    print(readC.getConfig_email(name='sender'))

