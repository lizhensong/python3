#!usr\bin\python3
#-*-coding:UTF-8-*-
#修改诗中某一个字
with open('./静夜思.txt','r') as file:
    fileword=file.read()
    str1 = fileword.replace('月', '日')
with open('./静夜思.txt','w') as file:
    num=file.write(str1)