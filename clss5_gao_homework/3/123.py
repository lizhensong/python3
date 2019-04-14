import csv


def cut(tibetan):
        tibetan_len = len(tibetan)
        tibetan_att = {'原字': tibetan, '前加字': None, '上加字': None, '基字': None, '下加字': None,
                       '再下加字': None, '元音': None, '后加字': None, '再后加字': None}
        # 判断叠字，元音
        tibetan_pile = []
        first = True
        i = 0
        while i < tibetan_len:
            if u'\u0F40' <= tibetan[i] < u'\u0F6D':  # 除叠字、元音外的普通字
                if first is False:
                    tibetan_att['后加字'] = tibetan[i]
                    i += 1
                    if i < tibetan_len:
                        tibetan_att['再后加字'] = tibetan[i]
                    else:
                        break
            elif u'\u0F8D' <= tibetan[i] < u'\u0FBD':  # 叠字
                if first:  # 遇到第一个叠字
                    if i is 2:
                        tibetan_att['前加字'] = tibetan[0]
                    tibetan_pile.append(tibetan[i - 1])
                    first = False
                    tibetan_pile.append(tibetan[i])
                else:  # 除第一个叠字之外其他叠字
                    tibetan_pile.append(tibetan[i])
            else:  # 元音
                tibetan_att['元音'] = tibetan[i]
                if first is True:  # 元音无叠字
                    tibetan_att['基字'] = tibetan[i - 1]
                    if i is 2:
                        tibetan_att['前加字'] = tibetan[0]
                first = False
                # 元音有无叠字都要处理
                i += 1
                if i < tibetan_len:
                    tibetan_att['后加字'] = tibetan[i]
                else:
                    break
                i += 1
                if i < tibetan_len:
                    tibetan_att['再后加字'] = tibetan[i]
                else:
                    break
            i += 1
        # 判断叠字
        if tibetan_pile:
            if len(tibetan_pile) is 2:
                if tibetan_pile[1] in ['ྱ', 'ྲ', 'ྭ', 'ླ']:
                    tibetan_att['基字'], tibetan_att['下加字'] = tibetan_pile[0], tibetan_pile[1]
                else:
                    tibetan_att['上加字'], tibetan_att['基字'] = tibetan_pile[0], tibetan_pile[1]
            else:
                if ''.join(tibetan_pile) in ['ཕྱྭ', 'གྲྭ']:
                    tibetan_att['基字'], tibetan_att['下加字'], tibetan_att['再下加字'] = \
                        tibetan_pile[0], tibetan_pile[1], tibetan_pile[2]
                else:
                    tibetan_att['上加字'], tibetan_att['基字'], tibetan_att['下加字'] = \
                        tibetan_pile[0], tibetan_pile[1], tibetan_pile[2]
        # 判断无叠字无元音(长度5，6，7一定有元音，叠字)
        if first is True:
            if tibetan_len is 4:
                tibetan_att['前加字'], tibetan_att['基字'], tibetan_att['后加字'], tibetan_att['再后加字'] \
                    = tibetan[0], tibetan[1], tibetan[2], tibetan[3]
            elif tibetan_len is 2:
                tibetan_att['基字'], tibetan_att['后加字'] = tibetan[0], tibetan[1]
            elif tibetan_len is 1:
                tibetan_att['基字'] = tibetan
            else:  # 长度为3
                if (tibetan[0] in ['ག', 'ད', 'བ', 'མ', 'འ'])and\
                        (tibetan not in ['བགས', 'མབས', 'གགས', 'བངས', 'དངས', 'གངས', 'འངས', 
                                         'གམས', 'མམས', 'བབས', 'མངས', 'གབས', 'བམས', 'འམམ']):
                    tibetan_att['前加字'], tibetan_att['基字'], tibetan_att['后加字'] = \
                        tibetan[0], tibetan[1], tibetan[2]
                else:
                    tibetan_att['基字'], tibetan_att['后加字'], tibetan_att['再后加字'] = \
                        tibetan[0], tibetan[1], tibetan[2]
        return [tibetan_att]


with open('./Tibetan_All.txt', 'r', encoding='utf-8') as fileR:
    tibetan_All = fileR.readlines()
with open('./Tibetan_All_Att.csv', 'w', newline='', encoding='utf-8')as csv_file:
    tibetan_att_list = ['原字', '前加字', '上加字', '基字', '下加字', '再下加字', '元音', '后加字', '再后加字']
    writer = csv.DictWriter(csv_file, tibetan_att_list)
    writer.writeheader()
    for tibetan_word in tibetan_All:
        writer.writerows(cut(tibetan_word[:-1]))
