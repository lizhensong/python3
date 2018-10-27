#!\usr\bin\python3
#-*-coding:utf-8-*-
#九九乘法表
for i in range(9):
    for j in range (i+1):
        print(i+1,'*',j+1,'=',(i+1)*(j+1))
    print('\n')