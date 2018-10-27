#!usr\bin\python3
# -*-coding:UTF-8-*-
# 上个TCP连接服务器的客户端
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


def socket_server_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('180.1.201.2', 9999))

    tcpsay = TcpSay('180.1.201.2', s)
    tcpwrite = TcpWrite('180.1.201.2', s)
    tcpsay.start()
    tcpwrite.start()
    tcpsay.join()
    tcpwrite.join()


def main():
    socket_server_client()


if __name__ == '__main__':
    main()
