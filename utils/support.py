"""一些支持方法，比如生成指定年龄的日期"""
import time
import datetime
from utils.log import logger
class Date():
    def birthday(self,date):
        start_year = int(time.strftime('%Y', time.localtime(time.time())))
        start_month = int(time.strftime('%m', time.localtime(time.time())))
        start_day = int(time.strftime('%d', time.localtime(time.time())))
        f = '%Y-%m-%d'
        if start_month-1==0:
            start_year=start_year-date-1
            start_month=12
            start_time = '{}-{}-{}'.format(start_year, start_month, start_day)
            # start_time=str(time.mktime(time.strptime(start_time, f)))
            start_time = str((datetime.datetime(start_year, start_month, start_day) - datetime.datetime(1970, 1, 1)).total_seconds())
            start_time=start_time[:-2]
        else:
            start_year = start_year - date
            start_month=start_month-1
            start_time = '{}-{}-{}'.format(start_year, start_month, start_day)
            # start_time = str(time.mktime(time.strptime(start_time, f)))
            start_time = str((datetime.datetime(start_year, start_month, start_day) - datetime.datetime(1970, 1,1)).total_seconds())
            start_time = start_time[:-2]
        return start_time

