from clss5_gao_homework.work6.cut import cut
import math
import time


def read_file_to_dict(path):
    with open(path, 'r', encoding='utf-8') as fileR:
        tibetan_all = fileR.readlines()
        tibetan_coding_all = []
        for tibetan_one in tibetan_all:
            data = cut(tibetan_one[:-1].strip('﻿'))
            tibetan_value = ''
            if u'\u0F8D' <= data['基字'] <= u'\u0FBD':
                tibetan_value += chr(ord(data['基字'])-80)
            else:
                tibetan_value += data['基字']
            if data['上加字']:
                tibetan_value += data['上加字']
            else:
                tibetan_value += chr(0x0001)
            if data['前加字']:
                tibetan_value += data['前加字']
            else:
                tibetan_value += chr(0x0001)
            if data['下加字']:
                tibetan_value += data['下加字']
            else:
                tibetan_value += chr(0x0001)
            if data['再下加字']:
                tibetan_value += data['再下加字']
            else:
                tibetan_value += chr(0x0001)
            if data['元音']:
                tibetan_value += data['元音']
            else:
                tibetan_value += chr(0x0001)
            if data['后加字']:
                tibetan_value += data['后加字']
            else:
                tibetan_value += chr(0x0001)
            if data['再后加字']:
                tibetan_value += data['再后加字']
            else:
                tibetan_value += chr(0x0001)
            tibetan_data = {'原字': data['原字'], '顺序字': tibetan_value}
            tibetan_coding_all.append(tibetan_data)
        return tibetan_coding_all


def sort(word, left, right):
    if left < right:
        middle = math.floor((right+left)/2)
        sort(word, left, middle)
        sort(word, middle+1, right)
        a = word[left:middle+1]
        b = word[middle+1:right+1]
        i = j = 0
        for k in range(left, right+1):
            if a[i]['顺序字'] < b[j]['顺序字']:
                word[k] = b[j]
                j += 1
            else:
                word[k] = a[i]
                i += 1
            if i > middle - left:
                word[k + 1:right+1] = b[j:]
                break
            if j > right - middle - 1:
                word[k + 1:right+1] = a[i:]
                break


if __name__ == '__main__':
    program_start = time.time()
    Tibetan_dict = read_file_to_dict('./Tibetan_All.txt')
    order_start = time.time()
    print('文件读取时间--{}'.format(order_start-program_start))
    sort(Tibetan_dict, 0, len(Tibetan_dict)-1)
    order_end = time.time()
    print('藏文排序时间--{}'.format(order_end - order_start))
    with open('./Tibetan_All_order.txt', 'w', encoding='utf-8') as file:
        for tibetan in Tibetan_dict:
            file.write(tibetan['原字'] + '\n')
    program_end = time.time()
    print('文件保存时间--{}'.format(program_end - order_end))
    print('程序运行总时间--{}'.format(program_end - program_start))
