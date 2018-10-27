#!usr\bin\python3
#-*-coding-utf-8-*-
#奇数和偶数的判断
print('奇数和偶数的判断(输入任意非数字退出)')
while(True):
    num=input('请输入')
    if num.isdigit():
        num=int(num)
        if num%2==0:
            print(num,'是偶数')
        else:
            print(num,'是奇数')
    else:
        break