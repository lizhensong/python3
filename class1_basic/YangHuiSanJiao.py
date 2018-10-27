#杨辉三角用generator实现
#!\usr\bin\python3
#-*-coding:UTF-8-*-
def odd(n):
    i,N=0,[1]
    while i<n:
        yield N
        N.insert(0,0)
        N.append(0)
        N=[N[j]+N[j+1] for j in range(i+2)]
        i=i+1

for x in odd(int(input())):
    print(x)
