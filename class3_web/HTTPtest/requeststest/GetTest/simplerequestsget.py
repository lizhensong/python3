#!usr\bin\python3
# -*-coding:UTF-8-*-
# python3中HTTP第三方包requests测试
import requests
# get
req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
r = requests.get('http://www.baidu.com/s', params={'ie': 'UTF-8', 'wd': 'python'}, headers=req_headers)
with open('test.html', 'wb') as f:
    f.write(r.text.encode('utf-8'))
print(r.text)
