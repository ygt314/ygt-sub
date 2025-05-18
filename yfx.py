from sys import path
path.append('mapyrc/')
from mymath import *
k=1
print("您正在计算函数坐标。")
while k<30:
    war=input("提示:\nDo you want to continue?(Y/n)")
    if war=="n"or war=="N":
        break
    print("第",k,"次计算")
    print("输入y=f(x)。x1,x0,dx只能是实数(或表达式)")
    funcx=input("y=")
    x0=float(eval(input("x0=")))
    x1=float(eval(input("x1=")))
    dx=float(eval(input("Δx=")))
    x,j=x0,0
    for i in range(100000):
        if dx>0:
            if x>x1:
                break
        if dx<0:
            if x<x1:
                break
        if dx==0:
            j+=1
            if j==10:
                break
        y=fx(funcx,x).real
        print("--->:({0:.9f}".format(x),",",y,")")
        x=x+dx
    k+=1
print("已退出")