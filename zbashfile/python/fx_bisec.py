import math as ma
import os
pi=ma.pi
sin=ma.sin
asin=ma.asin
cos=ma.cos
acos=ma.acos
tan=ma.tan
atan=ma.atan
e=ma.e
lg=ma.log10
ln=ma.log
log=ma.log
floor=ma.floor
fabs=ma.fabs
def f(x):
    y=eval(fx)
    return y
def bisec(a,b):
    print('begin-range>x∈(',a,',',b,')')
    while fabs(a-b)>=s:
        c=(a+b)/2
        if f(a)*f(c)<0:
            b=c
        elif f(c)==0:
            a=c;break
        else:
            a=c
        print('x∈(',a,',',b,')')
    print("(",i,") equation>",fx,"=0");print("(",i,") x≈",a)
i=1
print('------------------------------------------')
print('自变量:x,退出:quit|exit\n清屏:clear,库函数:ma.[func]')
print('--------------------------------------+')
while i<50:
    fx=input('function>')
    print('--------------------------------------+')
    if fx=="quit" or fx=="exit":
        print('END');break
    elif fx=="clear":
        os.system("clear")
    if fx!="quit" and fx!="clear" and fx!="":
        s=float(input('ε='));print('begin-range>x∈(a0,b0)')
        a=float(input('a0='));b=float(input('b0='))
        bisec(a,b);i+=1
        print('--------------------------------------+')