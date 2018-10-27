#!usr\bin\python3
#-*-coding:UTF-8-*-
#计算一元二次方程的解
from math import *
def quadratic(a,b,c):
    num1=(-b+sqrt(b*b-4*a*c))/(2*a)
    num2=(-b-sqrt(b*b-4*a*c))/(2*a)
    return num1,num2
a=int(input('a'))
b=int(input('b'))
c=int(input('c'))
print(quadratic(a,b,c))