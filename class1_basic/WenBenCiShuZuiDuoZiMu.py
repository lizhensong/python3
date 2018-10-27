#!usr\bin\python3
#-*-coding:UTF-8-*-
#找出文本中出现最多的字母
def ConWord(s):
    for i in s:
        if i.isalpha():
            return True
    return False
def NumMax(s):
    wordnum = {'word': None, 'num': 0}
    for i in s:
        if i.isalpha():
            num1 = s.count(i)
            if num1 > wordnum['num']:
                wordnum['word'] = i
                wordnum['num'] = num1
            elif num1 == wordnum['num']:
                if i < wordnum['word']:
                    wordnum['word'] = i
            s = s.replace(i, '')
    return wordnum
string=input('请输入包含字母的文本')
if ConWord(string)==True:
    string1=string.lower()
    print(NumMax(string1))
else:
    print('无字母')