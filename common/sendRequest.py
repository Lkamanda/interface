from common.readExcal import readExcel
from common.writeExcal import writeExcal
from common.configHttp import configHttp

class readWrite(object):
    def __init__(self):
        self.readE = readExcel()
        self.dataList = self.readE.assembleData()
        self.configH = configHttp()

    def get_url(self,  id):
        return self.dataList[id - 1][1]

    def get_httpMethod(self, id):
        return self.dataList[id - 1][2]

    def get_data(self, id):
        return eval(self.dataList[id - 1][4])

    def send_request(self, id):
        if self.get_httpMethod(id) == 'post' or self.get_httpMethod(id) == 'POST':
            res = self.configH.post(
                url=self.get_url( id),
                data=self.get_data(id)
            )
        elif self.get_httpMethod(id) == 'get':
            res = self.configH.get(
                url=self.get_url(id),
            )

        return res