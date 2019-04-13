import csv

with open('./Tibetan_All.txt', 'r', encoding='utf-8') as fileR:
    tibetan_All = fileR.readlines()
tibetan_All_Att = []
for tibetan in tibetan_All:
    tibetan = tibetan[:-1]
    tibetan_len = len(tibetan)
    tibetan_Att = {'原字': tibetan, '前加字': None, '上加字': None, '基字': None, '下加字': None,
                   '再下加字': None, '元音': None, '后加字': None, '再后加字': None}
    # 判断叠字，元音
    tibetan_pile = []
    first = True
    for i in range(tibetan_len):
        if tibetan[i] in range(0x0F00, 0x0F6C):  # 除叠字、元音外的普通字
            if first is False:
                tibetan_Att['后加字'] = tibetan[i]
                i += 1
                if i < tibetan_len:
                    tibetan_Att['再后加字'] = tibetan[i]
                else:
                    break
        elif tibetan[i] in range(0x0F8B, 0x0FDB):  # 叠字
            if first:  # 遇到第一个叠字
                if i is 2:
                    tibetan_Att['前加字'] = tibetan[0]
                tibetan_pile.append(tibetan[i - 1])
                first = False
                tibetan_pile.append(tibetan[i])
            else:  # 除第一个叠字之外其他叠字
                tibetan_pile.append(tibetan[i])
        else:  # 元音
            tibetan_Att['元音'] = tibetan[i]
            if first is True:  # 元音无叠字
                tibetan_Att['基字'] = tibetan[i - 1]
                if i is 2:
                    tibetan_Att['前加字'] = tibetan[0]
            first = False
            # 元音有无叠字都要处理
            i += 1
            if i < tibetan_len:
                tibetan_Att['后加字'] = tibetan[i]
            else:
                break
            i += 1
            if i < tibetan_len:
                tibetan_Att['再后加字'] = tibetan[i]
            else:
                break
    # 判断叠字
    if tibetan_pile:
        if len(tibetan_pile) is 2:
            tibetan_Att['上加字'] = tibetan_pile[0]
            tibetan_Att['基字'] = tibetan_pile[1]
        else:
            tibetan_Att['上加字'] = tibetan_pile[0]
            tibetan_Att['基字'] = tibetan_pile[1]
            tibetan_Att['下加字'] = tibetan_pile[2]
    # 判断无叠字无元音(长度5，6，7一定有元音，叠字)
    if first is True:
        if tibetan_len is 4:
            tibetan_Att['前加字'] = tibetan[0]
            tibetan_Att['基字'] = tibetan[1]
            tibetan_Att['后加字'] = tibetan[2]
            tibetan_Att['再后加字'] = tibetan[3]
        elif tibetan_len is 2:
            tibetan_Att['基字'] = tibetan[0]
            tibetan_Att['后加字'] = tibetan[1]
        elif tibetan_len is 1:
            tibetan_Att['基字'] = tibetan
        else:  # 长度为3
            tibetan_Att['前加字'] = tibetan[0]
            tibetan_Att['基字'] = tibetan[1]
            tibetan_Att['后加字'] = tibetan[2]
    print(tibetan_Att)
    tibetan_All_Att.append(tibetan_Att)
with open('./Tibetan_All_Att.csv', 'w', newline='', encoding='utf-8')as csv_file:
    writer = csv.DictWriter(csv_file, tibetan_All_Att[0].keys())
    writer.writeheader()
    writer.writerows(tibetan_All_Att)
