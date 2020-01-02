import unittest
from common.readExcal import readExcel
from common.writeExcal import writeExcal
from common.configHttp import configHttp


class ChatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 测试数据读取
        cls.readE = readExcel()
        cls.dataList = cls.readE.assembleData()
        # 测试数据写入




    def test1(self):
        print('test1')
        print(self.dataList)
        print('test2')




if __name__ == '__main__':
