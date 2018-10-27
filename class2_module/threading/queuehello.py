#!usr\bin\python3
#-*-coding:UTF-8-*-
#使用Queue实现生产者和消费者，Queue满提醒，Queue空提醒，Queue从空到产生唤醒睡眠的消费者。
import threading
import queue
import time
import random
class Producer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self)
        self.name=name
        self.queue=queue
    def run(self):
        while(True):
            if(self.queue.full()):
                print('盘子装了10个铜锣烧，满了，李震松师傅挂起10s')
                print('盘中铜锣烧：', self.queue.qsize(), '个')
                time.sleep(10)
                print('李震松师傅挂起结束')
            else:
                print('李震松师傅生产一个罗，休息一会')
                self.queue.put('铜锣烧')
                print('盘中铜锣烧：', self.queue.qsize(), '个')
                time.sleep(random.randrange(0,20))
                print('李震松师傅休息结束')
class Consumer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self)
        self.name=name
        self.queue=queue
    def run(self):
        while(True):
            if(self.queue.empty()):
                print('盘子中没有铜锣烧了，罗猪挂起10s')
                print('盘中铜锣烧：', self.queue.qsize(), '个')
                time.sleep(10)
                print('罗猪挂起结束')
            else:
                print('罗猪吃了一个罗，休息一会')
                self.queue.get()
                print('盘中铜锣烧：', self.queue.qsize(), '个')
                time.sleep(random.randrange(0, 20))
                print('罗猪休息结束')
def main():
    q=queue.Queue(10)
    producer=Producer('生产者',q)
    consumer=Consumer('消费者',q)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
if __name__=='__main__':
    main()