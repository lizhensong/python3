#!usr\bin\python3
#-*-coding:UTF-8-*-
#向一个文件中写入诗
shi=['     静夜思(李白)\n','床前明月光，疑似地上霜。\n','举头望明月，低头思故乡。']
f=open('./静夜思.txt','w')
f.writelines(shi)
