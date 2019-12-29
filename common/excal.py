# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-29 14:27
@Author  : zhoujialin
@File    : excal.py
'''
import xlrd

class readExcel(object):

    def __init__(self):
        readbook = xlrd.open_workbook(r"../testData/data.xls")
        self.urlsheet = readbook.sheet_by_index(0)
        self.paramsheet = readbook.sheet_by_name('paramSheet')
        self.assertsheet = readbook.sheet_by_index(2)

    def getSheetData(self,sheetName):
        # 获取行数
        sheetLineNum = sheetName.nrows
        data = []
        for i in range(1, sheetLineNum):
            # 获取这一行的所有页
            url_data = sheetName.row_values(i)
            data.append(url_data)
        return data

    def assembleData(self):
        urllist = self.getSheetData(self.urlsheet)
        paramlist = self.getSheetData(self.paramsheet)
        assertlist = self.getSheetData(self.assertsheet)
        data = []
        for i in range(len(urllist)):
            new_url = urllist[i]
            print(urllist[i])
            new_param = paramlist[i][1:]
            print()
            new_assert = assertlist[i][1:]

            new_url.extend(new_param)
            new_url.extend(new_assert)
            data.append(new_url)

        return data



if __name__ == '__main__':
    # re = readExcal()
    # print(re.assembleData())
    # all_data = re.assembleData()
    pass