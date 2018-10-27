#!usr\bin\python3

# python3的web开发，使用python内置的WSGI服务器，wsgiref模块

# application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。
# start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器
    return [b'<h1>hello,web!</h1>']
