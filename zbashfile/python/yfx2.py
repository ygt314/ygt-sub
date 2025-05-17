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
    print("输入y=f(x)。x1,x0,dx仅支持整数")
    funcx=input("y=")
    x0=int(input("x0="))
    x1=int(input("x1="))
    dx=int(input("Δx="))
    j=0
    if dx==0:
        while j<10:
            y=eval(funcx)
            x=x0
            print("--->:(",x,",",y,")")
            j+=1
    else:
        for x in range(x0,x1,dx):
            y=eval(funcx)
            print("--->:(",x,",",y,")")
    k+=1
print("已退出")