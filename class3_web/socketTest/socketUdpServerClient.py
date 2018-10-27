#!usr\bin\python3
# -*-coding:UTF-8-*-
# socket的UDP的客户端
import socket


def socket_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b'add', (socket.gethostname(), 9999))
    s.recv(1024).decode('utf-8')


def main():
    socket_client()


if __name__ == '__main__':
    main()