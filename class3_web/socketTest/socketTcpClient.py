#!usr\bin\python3
# -*-coding:UTF-8-*-
# TCP客户端连接
import socket


def socket_client():
    # 创建socket对象 socket.socket(family,type)
    # family是调用者期待返回的套接口地址的结构类型。eg.socket.AF_INET(IPV4地址类型)，socket.AF_INET6(IPV6地址类型)
    # type是套接字类型，面向连接（socket.SOCK_STREAM流套接字）和非连接（socket.SOCK_DGRAM数据报文套接字）
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 主动初始化TCP服务器连接。参数address是一个由ip地址（域名）和端口号组成的一个元组。
    # 函数有connect（address）如果连接出错，返回socket.error错误；
    # 当函数为connect_ex(address)它为connect的扩展版本，出错时返回错码而不是抛出异常
    s.connect(('www.baidu.com', 80))
    # 发送TCP数据，将string中的数据发送到连接的套接字
    # send()返回值是要发送的字节数量，该数量可能小于string的字节大小
    # sendall()在返回前尝试发送所有的数据，成功返回None，失败抛出异常
    s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
    # 接收返回数据 接收到的是二进制数据流
    buffer = []
    while True:
        # 接收TCP数据，以字符串形式返回 recv(bufsize) bufsize指定要接收的最大数据量
        # 每次最多接收1K字节
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    s.close()
    # 将接收到的列表数据组合成一个字符串
    data = b''.join(buffer)
    # 根据两个回车换行将字符串分割为header和html俩部分
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件
    with open('baidu.html', 'wb')as f:
        f.write(html)


def main():
    socket_client()


if __name__ == '__main__':
    main()
