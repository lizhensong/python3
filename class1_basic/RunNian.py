#!usr\bin\python3
#-*-coding:utf-8-*-
#闰年判断
print('闰年判断（输入0退出）')
while(True):
    time=input('请输入时间：')
    if time.isdigit():
        time=int(time)
        if time==0:
            break
        elif (time%4==0 and time%100!=0)or time%400==0:
            print(time,'年是闰年')
        else:
            print(time,'年不是闰年')
    else:
        print('请输入正确的时间')