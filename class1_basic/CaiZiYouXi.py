#!usr\bin\python3
#-*-coding:utf-8-*-
#猜字游戏
import random
num=random.randint(1,100)#1~100随机数
print('1~100数字猜测\n')
while(True):
    num1=input('请输入：')
    if num1.isdigit():
        num1=int(num1)
        if num1==num:
            print('猜测正确')
            break
        elif num1>num:
            print('数字大了')
        else:
            print('数字小了')
    else:
        print('请输入数字')