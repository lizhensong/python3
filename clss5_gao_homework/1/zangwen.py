with open('./Tibetan.txt', 'w', encoding='utf-8') as file:
    for Tibetan in range(0x0F00, 0x0FDB):
        file.write(chr(Tibetan)+'\n')
