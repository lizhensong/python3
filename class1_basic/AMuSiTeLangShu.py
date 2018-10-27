#!usr\bin\python3
#-*-coding:UTF-8-*-
#判断一个数是不是阿姆斯特朗数 n位正整数等于各位数字n次方的和
print('阿姆斯特朗数的判断(输入任意非数字退出)')
while(True):
    num=input('请输入')
    if num.isdigit():
        n=len(num)#测试数的长度
        num=int(num)
        i=n-1
        nadd=0
        num1=num
        while(i>=0):
            if i==0:
                nadd+=num1**n
            else:
                nadd+=(num1//10**i)**n
                num1%=10**i
            i-=1
        if num==nadd:
            print(num,'是阿姆斯特朗数')
        else:
            print(num,'不是阿姆斯特朗数')
    else:
        break