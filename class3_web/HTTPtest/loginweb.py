#!usr\bin\python3
# 登录某个网站，将登录返回写入html文件，直接单击该文件可以进入网站，对返回结果进行分析，提取一些有用信息。
# js网站无力
import requests
import json


def login_web(url, headers):

    d = {'username': 'admin', 'password': 'password'}
    res_obj = requests.post(url, data=d)
    # 爬取网址直接编码改为返回response对象的编码，杜绝乱码。
    print(res_obj.headers)
    print(res_obj.text.encode(res_obj.encoding))
    with open('test.html', 'wb') as f:
        f.write(res_obj.text.encode(res_obj.encoding))


def main():
    req_url = 'http://127.0.0.1:5000/sign_in'
    # win10，chrome浏览器
    req_headers = {
        'Accept':
            'text / html, application / xhtml + xml, application / xml;'
            'q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept - Encoding':
            'gzip, deflate, br',
        'Accept - Language':
            'zh - CN, zh;q = 0.9',
        'Cache - Control':
            'max - age = 0',
        'Connection':
            'keep - alive',
        'Content-Type':
            'application/x-www-form-urlencoded',
        'Upgrade - Insecure - Requests':
            '1',
        'User - Agent':
            'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) '
            'Chrome / 69.0.3497.92Safari / 537.36'}
    login_web(req_url, req_headers)


if __name__ == '__main__':
    main()
