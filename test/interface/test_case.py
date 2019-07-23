import unittest
from utils.config import Config
from utils.client import HTTPClient
from utils.log import logger
from utils.assertion import assertStr,cut
from utils.file_reader import ExcelReader
from utils.support import Date
class Test_case(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        pass

    # def test_login(self):
    #     test_login_url = self.URL + 'login.json'
    #     self.client = HTTPClient(url=test_login_url, method='POST')
    #     param = 'accessToken=&appVersionName=3.9.4&blackBoxType=SPARTA&blockBox=OFWfB5zSuB40pwdMdO%2BYb8FCghum7M0zStHMe1fkb4qa4TftNNPQIs/fXF/Zxqn7LuF0Peyiwyf6MHRLD7e75EwIqYeWtul6cRuuPA%2B9dTaM4DPYcnL4YyXTdS2X%2BRgUII/gb/9%2Bw2gkc4z8vNSSbc2ZnNglcjp5e7wJC6WXb4GPyi9DSEy4wJjjUuHThvHuhk1KizeOUzEFeqL1Lkr%2BSQX8iNbGzHLXHY1vOzTUwnHfIy0Hx%2BYmYEC1x5JLSklb9HMwy2HA9Xd0UpifAdSwjaLkbVTQTq56FgiuPRWyYv5avuAtp/xn48MOMLRDpRmXGPC24BeHkXW7KFqlC7FaYYWBp4tvBODhPYttYsb4sxlmxcnbX0/6AQ2BCQpP8H7LeTbcDhUQFor8m7E7y%2B0goO%2B9hg3IxRRBFaavkiFyr96ApuLosat1NpRJUOZoUGIibIY7KWa2I/NupvadYxgp767%2BUXHTIT2VjJdwcIDziqFf9%2BmyMWUSA97%2BniLz6JJLI/VTUofN03UNgvIJ0HEfeq7%2BUXHTIT2VjJdwcIDziqGkPqXYvu4%2BuSh1Fi1samz7c50Q23mPB0ABEo8YUd8zUuSELGj7cWC6FmdeeEW%2B69x0T0OTF2CSSRS6k6wboLUEZFFvpJP39vBLchUOunVQkfhZElJgOMjAeG50E4BXiyYAMFPJUrM2N0sWmVHOYVNjHaHCXK%2Bu5EdvvjU47jFwMOg9q4eaXPenQYCZTZWE0G9eB2iZGaGPGbN/NqXVvxHtFeu7Hhbb8QuJCP07bLHlLzfpJ4WTbg6qKVQwa6qTVl6TZ7SF1tbHfsZslgK%2B74KluJQsOlM/r3sEgUmodebnPmwSpWnFDbTh4805FGyu/ZM%3D&channel=App_Store&deviceId=C3B550FE-DFAB-4F03-A7A6-99519F88FD08&deviceType=iPhone&iphoneDesc=Simulator&iphoneType=x86_64&language=zh&netType=1&phone=18611379850&platform=1&resolution=%7B375%2C%20812%7D&screenSize=11&smsCode=123456&timestamp=1559042444&userId=&vendorId=75E3E4F0-C821-4988-8E37-12C0A466F61D&version=1.0.1'
    #     res = self.client.send(params=param)
    #     logger.debug(res.text)
    #     token = cut(res.text, 'ssToken":"', '","phone"')
    #     return token


    # def test_calcPrice(self):
    #     token=self.test_login()
    #     test_calcPrice_url=self.URL+'calcPrice.json'
    #     self.client = HTTPClient(url=test_calcPrice_url, method='GET')
    #     list = ExcelReader('C:/Users/Administrator/Desktop/Test_framework-master/data/interface.xlsx',title_line=False).data
    #     birtday = str(Date().birthday(int(list[1][1])))
    #     param='accessToken='+ token +'&appVersionName=3.9.3&birthday='+birtday+'&channel=App_Store&deviceId=2200C80B-0CB1-41C6-8DC2-8B00D9DAD3DE&deviceType=iPhone&insuranceId=32&insuranceScheme=%7B%0A%20%20%22insPlan%22%20%3A%20%222000000%22%2C%0A%20%20%22safePeriod%22%20%3A%20%225%22%2C%0A%20%20%22insurantBirthday%22%20%3A%20%2228%E5%A4%A9-65%E5%91%A8%E5%B2%81%22%0A%7D&insurants=%5B%7B%22insurantIdType%22%3A1%2C%22id%22%3A%22911324%22%2C%22insurantName%22%3A%22%E9%9F%A9%E9%A3%9E%E9%9B%AA%22%2C%22insurantNo%22%3A%223700%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A7567%22%2C%22birthday%22%3A393264000%2C%22hasSocialSecurity%22%3A1%2C%22insurantIsSelf%22%3A%221%22%2C%22relation%22%3A%221%22%2C%22sex%22%3A2%2C%22insurantPhone%22%3A%2218800004357%22%2C%22insurantPermanentResidence%22%3A%222%22%7D%5D&iphoneDesc=iPhone%208&iphoneType=iPhone10%2C1&language=zh&netType=1&period=5&platform=1&resolution=%7B375%2C%20667%7D&screenSize=11&sex=2&shareLimit=1&supportCase=770&timestamp=1558931127&userId=911324&vendorId=4F617898-ABF2-4D79-991A-EDBC7C9EA8E4&version=1.0.1'
    #     res = self.client.send(params=param)
    #     logger.debug(res.text)
    #     # logger.debug(ExcelReader('C:/Users/Administrator/Desktop/Test_framework-master/data/interface.xlsx', title_line=False).data)
    #     assertStr(res.text, 'harePrize":', ',"hasBoundB', '2')
    #     #self.assertIn('百度一下，你就知道', res.text)

    def test_calcPrice(self):
        test_calcPrice_url=self.URL + 'calcPrice.json'
        '''plus100万有社保'''
        for i in range(1,13):
            list=ExcelReader('C:/Users/Administrator/Desktop/Test_framework-master/data/interface.xlsx', sheet='e生保plus',title_line=False).data
            birtday=str(Date().birthday(int(list[i][1])))
            param='accessToken=CSddCECfcCncynT09LOII3g7352Ke36U&appVersionName=3.9.3&birthday=641660400&channel=App_Store&deviceId=24FD57FF-5EB7-4E89-8AAF-566B1A421F78&deviceType=iPhone&insuranceId=32&insuranceScheme={  "insPlan" : "2000000",  "safePeriod" : "5",  "insurantBirthday" : "28天-60周岁"}&insurants=[{"insurantIdType":1,"id":"6916140","insurantName":"刘思思","insurantNo":"4106**********9203","birthday":'+birtday+',"hasSocialSecurity":1,"insurantIsSelf":"1","relation":"1","sex":1,"insurantPhone":"18601122321","insurantPermanentResidence":"2"}]&iphoneDesc=Simulator&iphoneType=x86_64&language=zh&netType=1&period=5&platform=1&resolution={414, 896}&screenSize=11&sex=1&shareLimit=1&supportCase=770&timestamp=1559886348&userId=6916140&vendorId=8A58C566-68D1-494C-9899-32BF781BCC0B&version=1.0.1'
            self.client = HTTPClient(url=test_calcPrice_url, method='GET')
            res = self.client.send(params=param)
            price=str(list[i][2])
            assertStr(res.text, 'price":', ',"limit', price)
            logger.debug(res.text)
        '''plus100万无社保'''
        for i in range(14,26):
            list=ExcelReader('C:/Users/Administrator/Desktop/Test_framework-master/data/interface.xlsx', sheet='e生保plus',title_line=False).data
            birtday=str(Date().birthday(int(list[i][1])))
            param='accessToken=CSddCECfcCncynT09LOII3g7352Ke36U&appVersionName=3.9.3&birthday=641660400&channel=App_Store&deviceId=24FD57FF-5EB7-4E89-8AAF-566B1A421F78&deviceType=iPhone&insuranceId=32&insuranceScheme={  "insPlan" : "2000000",  "safePeriod" : "5",  "insurantBirthday" : "28天-60周岁"}&insurants=[{"insurantIdType":1,"id":"6916140","insurantName":"刘思思","insurantNo":"4106**********9203","birthday":'+birtday+',"hasSocialSecurity":2,"insurantIsSelf":"1","relation":"1","sex":1,"insurantPhone":"18601122321","insurantPermanentResidence":"2"}]&iphoneDesc=Simulator&iphoneType=x86_64&language=zh&netType=1&period=5&platform=1&resolution={414, 896}&screenSize=11&sex=1&shareLimit=1&supportCase=770&timestamp=1559886348&userId=6916140&vendorId=8A58C566-68D1-494C-9899-32BF781BCC0B&version=1.0.1'
            self.client = HTTPClient(url=test_calcPrice_url, method='GET')
            res = self.client.send(params=param)
            price=str(list[i][2])
            assertStr(res.text, 'price":', ',"limit', price)
            logger.debug(res.text)

        '''plus300万有社保'''
        for i in range(27,39):
            list=ExcelReader('C:/Users/Administrator/Desktop/Test_framework-master/data/interface.xlsx', sheet='e生保plus',title_line=False).data
            birtday=str(Date().birthday(int(list[i][1])))
            param='accessToken=CSddCECfcCncynT09LOII3g7352Ke36U&appVersionName=3.9.3&birthday=641660400&channel=App_Store&deviceId=24FD57FF-5EB7-4E89-8AAF-566B1A421F78&deviceType=iPhone&insuranceId=32&insuranceScheme={  "insPlan" : "6000000",  "safePeriod" : "5",  "insurantBirthday" : "28天-60周岁"}&insurants=[{"insurantIdType":1,"id":"6916140","insurantName":"刘思思","insurantNo":"4106**********9203","birthday":'+birtday+',"hasSocialSecurity":1,"insurantIsSelf":"1","relation":"1","sex":1,"insurantPhone":"18601122321","insurantPermanentResidence":"2"}]&iphoneDesc=Simulator&iphoneType=x86_64&language=zh&netType=1&period=5&platform=1&resolution={414, 896}&screenSize=11&sex=1&shareLimit=1&supportCase=771&timestamp=1559886348&userId=6916140&vendorId=8A58C566-68D1-494C-9899-32BF781BCC0B&version=1.0.1'
            self.client = HTTPClient(url=test_calcPrice_url, method='GET')
            res = self.client.send(params=param)
            price=str(list[i][2])
            assertStr(res.text, 'price":', ',"limit', price)
            logger.debug(res.text)

        '''plus300万无社保'''
        for i in range(40,52):
            list=ExcelReader('C:/Users/Administrator/Desktop/Test_framework-master/data/interface.xlsx', sheet='e生保plus',title_line=False).data
            birtday=str(Date().birthday(int(list[i][1])))
            param='accessToken=CSddCECfcCncynT09LOII3g7352Ke36U&appVersionName=3.9.3&birthday=641660400&channel=App_Store&deviceId=24FD57FF-5EB7-4E89-8AAF-566B1A421F78&deviceType=iPhone&insuranceId=32&insuranceScheme={  "insPlan" : "6000000",  "safePeriod" : "5",  "insurantBirthday" : "28天-60周岁"}&insurants=[{"insurantIdType":1,"id":"6916140","insurantName":"刘思思","insurantNo":"4106**********9203","birthday":'+birtday+',"hasSocialSecurity":2,"insurantIsSelf":"1","relation":"1","sex":1,"insurantPhone":"18601122321","insurantPermanentResidence":"2"}]&iphoneDesc=Simulator&iphoneType=x86_64&language=zh&netType=1&period=5&platform=1&resolution={414, 896}&screenSize=11&sex=1&shareLimit=1&supportCase=771&timestamp=1559886348&userId=6916140&vendorId=8A58C566-68D1-494C-9899-32BF781BCC0B&version=1.0.1'
            self.client = HTTPClient(url=test_calcPrice_url, method='GET')
            res = self.client.send(params=param)
            price=str(list[i][2])
            assertStr(res.text, 'price":', ',"limit', price)
            logger.debug(res.text)





















