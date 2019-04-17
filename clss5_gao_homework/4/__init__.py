import csv
import time


def read_csv_file_dict(path):
    with open(path, encoding='utf-8')as csv_file:
        reader = csv.DictReader(csv_file)
        tibetan_coding_all = []
        for data in reader:
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


if __name__ == '__main__':
    program_start = time.time()
    Tibetan_dict = read_csv_file_dict('./Tibetan_All_Att.csv')
    order_start = time.time()
    print('文件读取时间--{}'.format(order_start-program_start))
    t_num = len(Tibetan_dict)
    for i in range(1, t_num):
        j = k = i
        while j > 0:
            j -= 1
            if Tibetan_dict[k]['顺序字'] < Tibetan_dict[j]['顺序字']:
                Tibetan_dict[k], Tibetan_dict[j] = Tibetan_dict[j], Tibetan_dict[k]
                k = j
    order_end = time.time()
    print('藏文排序时间--{}'.format(order_end - order_start))
    with open('./Tibetan_order.txt', 'w', encoding='utf-8') as file:
        for tibetan in Tibetan_dict:
            file.write(tibetan['原字'] + '\n')
    program_end = time.time()
    print('文件保存时间--{}'.format(program_end - order_end))
    print('程序运行总时间--{}'.format(program_end - program_start))
