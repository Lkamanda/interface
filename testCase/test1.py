import unittest
from common.sendRequest import readWrite
readwrite = readWrite()

class ChatTest(unittest.TestCase):
    @classmethod
    # def setUpClass(cls):
    #     # 测试数据读取
    #     #  此id 和 excal 表中保持一致
    #     cls.id =  2
    #     cls.readE = readExcel()
    #     cls.dataList = cls.readE.assembleData()
    #     # 测试数据写入
    #     cls.url = cls.dataList[cls.id-1][1]
    #     cls.http_method = cls.dataList[cls.id-1][2]
    #     cls.data = cls.dataList[cls.id-1][4]
    #
    #     # cls.assert_except = cls.dataList[cls.id-1][5]
    #     # cls.assert_real = cls.dataList[cls.id-1][6]
    #     # cls.result = cls.dataList[cls.id-1][7]
    #     cls.configH = configHttp()

    def setUp(self):
        pass

    def test1(self):
        id = 1
        print('test1')
        print(readwrite.get_data(id))
        print('test2')

    def test2(self):
        id = 1
        res = readwrite.send_request(id)
        print('这是json',res.json())


    # def test3(self):
    #     # id = 2
    #     # print(get_data(dataList, id))



if __name__ == '__main__':
    unittest.main()


