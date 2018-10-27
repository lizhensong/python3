#!usr\bin\python3
#-*-coding:UTF-8-*-
#输出上周一的日期和本周一的日期
import time
import datetime
from class2_module.timetest import qianjitiannianyueri
now=time.localtime()
thisweekday=now.tm_wday
thisyear=datetime.datetime.now().year
thismonth=datetime.datetime.now().month
thisday=datetime.datetime.now().day
print('今天：',thisyear,'-',thismonth,'-',thisday)
print('本周一：',qianjitiannianyueri.date(thisyear,thismonth,thisday,thisweekday))
print('上周一：',qianjitiannianyueri.date(thisyear,thismonth,thisday,thisweekday+7))