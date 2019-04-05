with open('./Tibetan_221.txt', 'r', encoding='utf-8') as fileR:
    tibetan_221 = fileR.readlines()
with open('./Tibetan_All.txt', 'w', encoding='utf-8') as fileW:
    fileW.writelines(tibetan_221)
    tibetan_221_vowel = []
    vowel = ['ི', 'ུ', 'ེ', 'ོ']
    for i in tibetan_221:
        tibetan_221_vowel.append(i[:-1])
        for j in vowel:
            word = i[:-1]+j
            fileW.write(word+'\n')
            tibetan_221_vowel.append(word)
    postAddition = ["ག", "ང", "བ", "མ", "ད", "ས", "ན", "ར", "ལ"]
    for i in tibetan_221_vowel:
        for j in postAddition:
            fileW.write(i+j+'\n')
    for i in tibetan_221_vowel:
        for j in postAddition[:-5]:
            fileW.write(i+j+'ས'+'\n')
    for i in tibetan_221_vowel:
        for j in postAddition[6:]:
            fileW.write(i+j+'ད'+'\n')
