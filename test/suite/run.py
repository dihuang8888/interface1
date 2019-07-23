import unittest
import time
from utils.mail import Email
from utils.config import Config, REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner

times = time.strftime("%m-%d %H-%M", time.localtime())
class Suite(unittest.TestSuite):
    def __init__(self,suite):
        self.suite = suite

    def runSuite(self):
        html_file = REPORT_PATH+'\\' + str(times) + '.html'
        fp = open(html_file, 'wb')
        runner = HTMLTestRunner(stream=fp, verbosity=2, title=u'测试报告', description=u'用例执行情况：')
        runner.run(self.suite)
        fp.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromName('test.interface.test_case.Test_case'))
    Suite(suite).runSuite()
    report = REPORT_PATH + '\\' + str(times) + '.html'
    e = Email(title='测试报告',
              message='这是本次的测试报告，请查收！',
              receiver='262689@qq.com',
              server='smtp.163.com',
              sender='18201291852@163.com',
              password='qwe452727',
              path=report
              )
    e.send()