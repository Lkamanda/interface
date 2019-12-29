# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-29 10:47
@Author  : zhoujialin
@File    : readExcal.py
'''

# 导入读取excal包
# 打开目标文件
# 定位sheet页
# 定位行和列
# 读取数据
# 组装数据
# return 数据

import xlrd

readbook = xlrd.open_workbook(r"../testData/data.xls")

print(readbook)
# url_sheet = readbook.sheet_by_name('sheet1')页
# 定位sheet
urlsheet = readbook.sheet_by_index(0)
paramsheet  = readbook.sheet_by_name('paramSheet')
assertsheet = readbook.sheet_by_index(2)

# 4定位行和列

def getSheetData(sheetName):
    # 获取行数
    sheetLineNum = sheetName.nrows
    data = []
    for i in range(1, sheetLineNum):
        # 获取这一行的所有页
        url_data = sheetName.row_values(i)
        data.append(url_data)
    return data

urlsheetData = getSheetData(urlsheet)
print(urlsheetData)
paramsheetData = getSheetData(paramsheet)
assertsheetData = getSheetData(assertsheet)

# print(urlsheetData)
# print(paramsheetData)
# print(assertsheetData)

# tmp = list(zip(urlsheetData,paramsheetData))
# print(tmp)
# data = list(zip(urlsheetData, paramsheetData))

def getDate(*args):
    r_list = []
    num = len(args)
    for arg in args:
        temp = []
        for i in range(num):
            temp.append(arg[i])
        r_list.append(temp)
    return r_list

data = getDate(urlsheetData, paramsheetData, assertsheetData)
print(data)




list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]


# r_list = []
# for i in range(3):
#     list4 = []
#     list4.append(list1[i])
#     list4.append(list2[i])
#     list4.append(list3[i])
#     r_list.append(list4)
# print(r_list)

data = getDate(urlsheetData, paramsheetData, assertsheetData)
print(data)
