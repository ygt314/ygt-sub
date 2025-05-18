"""
Use:plot2_sh.py f(x) [x] [y] [:]
version:1.65
==========
It's plot(x, y) for y=f(x)
May be:y=y+f(x,y)
May be:y=y+(fxy<0)(><)(it's black)
May be:y=y-1+(fxy<0)(><)(it's white)
==========
by 3414394513(QQ)@π3.141592653589793(YGT)
"""
import numpy as np
import sys
sys.path.append('mapyrc/')
from mymath import *
sv=sys.argv
# function
def px(n):
    sg='|' if abs(n)>dy/2 else '─→ₓ'
    return sg
def py(n):
    sg='-' if abs(n)>dx/2 else 'y'
    return sg
def ss(a,b):
    d=xsex((a*a+b*b)**0.5)
    return (a*a/d+b*b/d)*0.6
# data
m=-10;n=10 # inf is unlimed-num
x1,x2,y1,y2=-10,10,-10,10
vx='x1,x2=';vy='y1,y2=';vl=[vx,vy];vv='';xy=[",x∈",",y∈"]
if len(sv)>3:
    for i in range(2,4):
        vi='['+sv[i]+']' if (sv[i])[0]!="[" else sv[i]
        sl=eval(vi)
        if len(sl)==2:
            m=sl[1]-20;n=sl[0]+20
            exec(vl[i-2]+vi)
xl=np.linspace(float(x1),float(x2),80);xx=0
yl=[0]+np.linspace(float(y2),float(y1),40);yy=-1
vv+=xy[0]+str([x1,x2])+xy[1]+str([y1,y2])
# plot set
if len(sv)==5:
    p=str(sv[4])
else:
    p=str(sv[2]) if len(sv)==3 else ''
if len(p)==0:
    p=':'
# error
dx=(xl[3]-xl[2])
dy=(yl[2]-yl[3])
ds=dx*dx+dy*dy
# double x-length
# plot(x,y)
f=str(sv[1]) if len(sv)>1 else 'y'
print('f(x)='+f+vv)
for y in yl:
    xx=0;yy+=1
    for x in xl:
        if yy==0:
            print(end=py(x))
        elif yy==1 and py(x)=='y':
            print(end='|')
        elif x*x+y*y<ds/3:
            print(end='O')
        elif abs(y-xsex(eval(f)))<ss(dx,dy):
            print(end=p)
        else:
            print(end=' ')
        xx+=1
    print(px(y))