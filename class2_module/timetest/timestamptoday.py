#!usr\bin\python3
#-*-coding:UTF-8-*-
#昨天0点到今天0点整点的时间戳(月内可用)
import time
import datetime
now=datetime.datetime.now()
yday=now.day-1
yhour=0
#yminute=0
#ysecond=0
#ymicrosecond=0
while yhour<24:
    string=str(now.year)+' '+str(now.month)+' '+str(yday)+' '+str(yhour)
    print(string)
    struct_time=time.strptime(string,"%Y %m %d %H")
    print(struct_time)
    Timestamp=time.mktime(struct_time)
    print(Timestamp)
    yhour += 1