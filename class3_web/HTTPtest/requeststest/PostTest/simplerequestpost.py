#!usr\bin\python3
# -*-coding:UTF-8-*-
# python3中HTTP第三方包requests测试
import requests
import json
# post
req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
post_data = {'ie': 'UTF-8', 'wd': 'python'}
r = requests.post("http://www.baidu.com/s", data=json.dumps(post_data), headers=req_headers)
with open('test.html', 'wb') as f:
    f.write(r.text.encode('utf-8'))
print(r.text)
print(r.url, r.cookies, r.status_code, '\n', r.headers)