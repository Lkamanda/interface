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
import os


# configP = 'config.txt'
# # configPath = r'C:\Users\zhoujialin\PycharmProjects\interface\config.txt'
# # 怎么解决不使用绝对路径的问题
# configPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), configP)
# print(configPath)


class readConfig(object):

    def __init__(self):
        self.configP = 'config.txt'
        self.configPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), self.configP)
        self.cf = configparser.ConfigParser()
        self.cf.read(self.configPath, encoding='utf-8-sig')

    def getConfig_email(self, name):
        name = self.cf.get('email', name)
        return name


if __name__ == '__main__':
    readC = readConfig()
    print(readC.getConfig_email(name='sender'))

