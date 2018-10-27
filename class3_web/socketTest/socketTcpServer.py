#!usr\bin\python3
# -*-coding:UTF-8-*-
# TCP服务器端连接
import socket
import threading


class TcpSay(threading.Thread):
    def __init__(self, name, sock):
        threading.Thread.__init__(self)
        self.name = name
        self.sock = sock

    def run(self):
        while True:
            clientstr = input()
            self.sock.send(bytes(clientstr.encode('utf-8')))


class TcpWrite(threading.Thread):
    def __init__(self, name, sock):
        threading.Thread.__init__(self)
        self.name = name
        self.sock = sock

    def run(self):
        while True:
            print(self.sock.recv(1024).decode('utf-8'))


def socket_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 将socket绑定到指定地址。参数address是一个由ip地址（域名）和端口号组成的一个元组。
    # 函数有bind（address）如果连接出错，返回socket.error错误；
    s.bind((socket.gethostname(), 9999))
    # 设置最大连接数。listen(backlog) backlog 最小为1，如果队列满了，拒绝请求。
    s.listen(5)
    # accept(),被动接受客户端连接，等待连接到来
    while True:
        sock, addr = s.accept()
        print(addr, '连接')
        tcpsay = TcpSay(addr, sock)
        tcpwrite = TcpWrite(addr, sock)
        tcpsay.start()
        tcpwrite.start()


def main():
    socket_server()


if __name__ == '__main__':
    main()
