#!usr\bin\python3
#-*-coding:UTF-8-*-
#线程运行模拟构造函数

import threading
import time
import datetime

loops=[4,2]
date_time_format='%Y-%m-%d %H:%M:%S'

class MyTread(threading.Thread):
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
    def run(self):
        print('starting',self.name,'at',date_time_str(datetime.datetime.now()))
        self.func(*self.args)
        print('finished',self.name,'at',date_time_str(datetime.datetime.now()))
def date_time_str(date_time):
    return datetime.datetime.strftime(date_time,date_time_format)
def loop(n_loop,n_sec):
    print('线程', n_loop, '开始执行：', date_time_str(datetime.datetime.now()), '先休眠', n_sec, '秒')
    time.sleep(n_sec)
    print('线程', n_loop, '休眠结束，时间：', date_time_str(datetime.datetime.now()))
def main():
    print('所有线程开始执行：', date_time_str(datetime.datetime.now()))
    threads = []
    n_loops = range(len(loops))
    for i in n_loops:
        t = MyTread(loop,(i,loops[i]))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print('所有线程结束：', date_time_str(datetime.datetime.now()))


if __name__ == '__main__':
    main()