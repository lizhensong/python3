from clss5_gao_homework.work5.cut import cut

if __name__ == '__main__':
    with open('./Tibetan_All.txt', 'r', encoding='utf-8') as fileR:
        tibetan_All = fileR.readlines()
    dict_num = {'前加字': {}, '上加字': {}, '基字': {}, '下加字': {}, '再下加字': {}, '元音': {}, '后加字': {}, '再后加字': {}}
    for tibetan_word in tibetan_All:
        tibetan_att = cut(tibetan_word[:-1])
        for label in tibetan_att:
            if tibetan_att[label]:
                if u'\u0F8D' <= tibetan_att[label] <= u'\u0FBD':
                    tibetan_att[label] = chr(ord(tibetan_att[label]) - 80)
                if tibetan_att[label] in dict_num[label]:
                    dict_num[label][tibetan_att[label]] += 1
                else:
                    dict_num[label][tibetan_att[label]] = 1
    with open('./Tibetan_Att_num.txt', 'w', encoding='utf-8')as file:
        for i in dict_num:
            file.write(i+'\n')
            for j in dict_num[i]:
                file.write('{}:{}\n'.format(j, dict_num[i][j]))
