"""
version:1.53
==========
It's plot(x, y) for y=f(x)
May f(x,y)=0:y=y+f(x,y)
May f(x,y)<0(><):y=y+(fxy<0)(><)(it's black)
May f(x,y)<0(><):y=y-1+(fxy<0)(><)(it's white)
==========
by 3414394513(QQ)@π3.141592653589793(YGT)
"""
import sys
sys.path.append('mapyrc/')
from mymath import *
import numpy as np
# function
def px(n):
    s='─→ₓ'
    if abs(n)>dy/2:
        s='|'
    return s
def py(n):
    s='y'
    if abs(n)>dx/2:
        s='-'
    return s
def ss(a,b):
    d=xsex((a*a+b*b)**0.5)
    return (a*a/d+b*b/d)*0.6
# data
x1,x2,y1,y2=-10,10,-10,10
for xy in ['x1','x2','y1','y2']:
    vxy=input("[var "+xy+']:')
    if vxy!='':
        exec(xy+"="+vxy)
xl=np.linspace(x1,x2);xx=0
yl=[0]+np.linspace(y2,y1);yy=-1
# plot set
p=input("plot:>")
if p=='':
    p=':'
# error
dx=(xl[3]-xl[2])
dy=(yl[2]-yl[3])
ds=dx*dx+dy*dy
# half y-length
print("will half y-length")
# plot(x,y)
f=input("f(x)=")
for y in yl:
    xx=0;yy+=1
    if yy%2==1:
        continue
    for x in xl:
        if yy==0:
            print(end=py(x))
        elif yy==2 and py(x)=='y':
            print(end='|')
        elif x*x+y*y<ds/3:
            print(end='O')
        elif abs(y-xsex(eval(f)))<ss(dx,dy):
            print(end=p)
        else:
            print(end=' ')
        xx+=1
    print(px(y))