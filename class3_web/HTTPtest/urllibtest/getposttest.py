# usr\bin\python3
# -*-coding:UTF-8-*-
# 用urllib库实现python3的HTTP请求（eg. get,post...）
import urllib.request
import urllib.parse
'''
构造了Request对象，然后将其传入urlopen()函数中，返回一个Response对象；
因为只传入了一个url所以这个的提交方法自动选择是GET；
这个可以不用构造Request对象，直接将URL传入urlopen()函数中，返回Response对象。
'''
url_request = 'http://192.168.11.2/a70.htm'

# request_obj_get = urllib.request.Request(url_request)
# response_obj_get = urllib.request.urlopen(request_obj_get)
# html_code_get = response_obj_get.read().decode('utf-8', 'ignore')
# print(html_code_get)

'''
构造了Request对象，然后将其传入urlopen()函数中，返回一个Response对象；
因为传入了一个url，一个data,所以这个的提交方法自动选择是POST；
这个可以不用构造Request对象，直接将URL，data传入urlopen()函数中，返回Response对象。
'''
# data传输失败
post_data = urllib.parse.urlencode({'username': 'a', 'password': 'b'}).encode('utf-8')
# 请求头找到任一浏览器的Request Headers 模拟浏览器，win10，chrome浏览器
request_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
request_obj_post = urllib .request.Request(url=url_request, data=post_data, headers=request_header)
# 添加cookie
request_obj_post.add_header('Cookie', 'username="root", password="root"')
response_obj_post = urllib.request.urlopen(request_obj_post)
html_code_post = response_obj_post.read().decode('utf-8')
print(response_obj_post.headers, html_code_post)
