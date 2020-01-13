import unittest
from ddt import ddt, unpack,data
from common.readExcal import readExcel
from common.writeExcal import writeExcal
from common.configHttp import configHttp
from log.myLog import mylogger

testData = readExcel()
test_data = testData.assembleData()
print(testData)
configH = configHttp()
resultList=[]


@ddt
class ChatTest(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        writeE = writeExcal(status=resultList)
        writeE.write()


    @ddt
    @unpack
    @data(*test_data)
    def test_request(self, id, url, method, des,  param, expect, real,result):
        mylogger.debug(id, url, method, des,  param, expect, real,result)
        mylogger.debug('cesji')
        print('zheshi',id, url, method,des,  param, expect, real, result)
        print(method)
        param = eval(param)
        if method == 'get' or method == 'GET':
            real = configH.get(url=url, data=data)
            try:
                self.assertEqual(expect, str(real))
                result = 'success'
                resultList.append(result)
            except Exception as e:
                print(e)
                result = 'fail'
                resultList.append(result)
        elif method == 'post' or method =='POST':
            real = configH.post(url=url, param=param)
            print(expect, str(real))
            try:
                self.assertEqual(expect, str(real))
                result = 'success'
                resultList.append(result)
            except Exception as e:
                print(e)
                result = 'fail'
                resultList.append(result)


if __name__ == '__main__':
    mycase = ChatTest()
    mycase.main()




