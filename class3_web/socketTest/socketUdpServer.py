#!usr\bin\python3
# -*-coding:UTF-8-*-
# socket的UDP通讯服务器的建立
import socket
import threading


class Receive:
    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):

        pass


class Send:
    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):

        pass


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((socket.gethostname(), 9999))
    while True:
        # data 数据 addr 地址 ip和端口号
        data, addr = s.recvfrom(1024)
        # 发送
        s.sendto(b'asd', addr)
    pass


if __name__ == '__main__':
    main()
