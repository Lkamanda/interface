# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-29 14:27
@Author  : zhoujialin
@File    : readExcal.py
'''
import xlrd

class readExcel(object):

    def __init__(self):
        "/Users/zhoujialin/PycharmProjects/interface/testData/data_demo.xls"
        # readbook = xlrd.open_workbook(r"/testData/data_demo.xls")
        readbook = xlrd.open_workbook(r"./testData/data_demo.xls")

        self.urlSheet = readbook.sheet_by_index(0)
        self.paramSheet = readbook.sheet_by_name('paramSheet')
        self.assertSheet = readbook.sheet_by_index(2)

    def getSheetData(self,sheetName):
        # 获取行数
        sheetLineNum = sheetName.nrows
        data = []
        for i in range(1, sheetLineNum):
            # 获取这一行的所有页
            url_data = sheetName.row_values(i)
            if sheetName == self.urlSheet:
                url_data[1] = url_data[1] + url_data[2]
                url_data.pop(2)
            data.append(url_data)
        return data

    def assembleData(self):
        urlList = self.getSheetData(self.urlSheet)
        paramList = self.getSheetData(self.paramSheet)
        assertList = self.getSheetData(self.assertSheet)
        data = []

        for i in range(len(urlList)):
            new_url = urlList[i]
            new_param = paramList[i][1:]
            new_assert = assertList[i][1:]
            new_url.extend(new_param)
            new_url.extend(new_assert)
            data.append(new_url)
        return data

if __name__ == '__main__':
    re = readExcel()
    # print(re.assembleData())
    all_data = re.assembleData()
