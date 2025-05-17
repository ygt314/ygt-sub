import math as m
pi=m.pi
sin=m.sin
cos=m.cos
tan=m.tan
e=m.e
fabs=m.fabs
k=1
print("您正在计算函数坐标。\n一般三角函数和pi可以用原形。\n其它须正确输入形式")
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
    x=x0
    j=0
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
        y=eval(funcx)
        print("--->:({0:.9f}".format(x),",",y,")")
        x=x+dx
    k+=1
print("已退出")