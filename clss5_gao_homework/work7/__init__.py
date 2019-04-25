import os
import re
from collections import Counter


def getfilename(path):
    p_list = []
    f_list = os.listdir(path)
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.txt':
            path_document = path + '/' + i
            p_list.append(path_document)
    return p_list


if __name__ == '__main__':
    path_file = '.'
    path_list = getfilename(path_file)
    tibetan_counter = Counter({})
    for path_one in path_list:
        with open(path_one, 'r', encoding='utf-8') as fileR:
            tibetan = fileR.readline()
            while tibetan != '':
                tibetan_list = re.split(r'([\u0f00-\u0f1f\u0f34\u0f36\u0f38\u0f3a-\u0f3f\u0fbd-\u0fff]|'  # 标点和其他
                                        r'[\u0f20-\u0f33]+|'  # 数字
                                        r'[\u0f35\u0f37\u0f39\u0f40-\u0fbc]+[\u0f85]|'  # 以0f85结尾没有分隔符的
                                        r'[^\u0f00-\u0fff]+)',  # 非藏文
                                        tibetan)
                tibetan_counter.update(tibetan_list)
                tibetan = fileR.readline()
    with open('./Tibetan_All_Counter.txt', 'w', encoding='utf-8') as file:
        for one_num in tibetan_counter:
            file.write('{}={}\n'.format(one_num, tibetan_counter[one_num]))
