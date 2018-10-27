#!usr\bin\python3
#-*-coding:UTF-8-*-
#统计诗中文字的频率
import os
def gezifutongji(oldstr):
    newdirc={}
    while True:
        oldstr=oldstr.lstrip()
        if len(oldstr)!=0:
            index=oldstr.count(oldstr[0])
            newdirc.update({oldstr[0]:str(index)+'\n'})
            oldstr=oldstr.replace(oldstr[0],'')
        else:
            break
    return newdirc
with open('./静夜思.txt','r') as file:
    fileword=file.read();
    try:
        os.remove('./统计.txt')
    except:
        pass
    finally:
        dict1=gezifutongji(fileword)
        list1=[]
        for key in dict1.keys():
            list1.append(key+':'+dict1[key])
        with open('./统计.txt','w') as file:
            file.writelines(list1)
