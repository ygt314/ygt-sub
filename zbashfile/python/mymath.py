import math as ma
import cmath as cm
pi=ma.pi;i=1j;deg='d';rad='r';e=ma.e
s2=2**0.5;phi=(5**0.5-1)/2;gama=0.577
def r_d(r):
    return r/pi*180
def d_r(d):
    return d/180*pi
#尝试约化小数部分,但不处理整数,支持复数
def xsex(n,cale=12):
    ans=n
    if type(n) != int:
        f='.'+str(cale)+'g'
        ans=eval(format(n,f))
    ans=ans.imag*1j if abs(n.real)<10**(-cale) else ans
    return ans
#尝试得到实数
def cn_rn(c,cale=12):
    cc=xsex(c,cale)
    ans=cc.real if abs(c.imag)<10**(-cale) else cc
    return ans
#正弦
def sin(n,dd='r'):
    r=d_r(n) if dd==deg else n
    return cm.sin(r)
#余割
def csc(n,dd='r'):
    r=d_r(n) if dd==deg else n
    return 1/cm.sin(r)
#余弦
def cos(n,dd='r'):
    r=d_r(n) if dd==deg else n
    return cm.cos(r)
#正割
def sec(n,dd='r'):
    r=d_r(n) if dd==deg else n
    return 1/cm.cos(r)
#正切
def tan(n,dd='r'):
    r=d_r(n) if dd==deg else n
    return cm.tan(r)
#余切
def cot(n,dd='r'):
    r=d_r(n) if dd==deg else n
    return 1/cm.tan(r)
#反正弦
def asin(n,dd='r'):
    r=cm.asin(n)
    d=r_d(r) if dd==deg else r
    return d
#反余割
def acsc(n,dd='r'):
    r=cm.asin(1/n)
    d=r_d(r) if dd==deg else r
    return d
#反余弦
def acos(n,dd='r'):
    r=cm.acos(n)
    d=r_d(r) if dd==deg else r
    return d
#反正割
def asec(n,dd='r'):
    r=cm.acos(1/n)
    d=r_d(r) if dd==deg else r
    return d
#反正切
def atan(n,dd='r'):
    r=cm.atan(n)
    d=r_d(r) if dd==deg else r
    return d
#反余切
def acot(n,dd='r'):
    r=cm.atan(1/n)
    d=r_d(r) if dd==deg else r
    return d
lg=cm.log10;ln=cm.log;log=cm.log
floor=ma.floor;inf=10**12;s=1e-12
a,b,c,d=-7,-6,-5,-4
m,n=-3,-2
p,q=-1,1
x,y,z=2,3,4
u,v,w=5,6,7
ll,mm,rr='l','m','r'
def num(n):
    ans=False
    if type(n)==int or type(n)==float:
        ans=True
    elif type(n)==complex:
        ans=True
    return ans
def fx(f,n=x):
    global x
    x=n
    return eval(f)
def bisec(f,a=-100,b=100,s=1e-12):
    while abs(a-b)>=s:
        c=(a+b)/2;fa=cn_rn(fx(f,a));fc=cn_rn(fx(f,c))
        if type(fa)==complex or type(fc)==complex:
            a=c;continue
        if fa*fc<0:
            b=c
        elif fc==0:
            a=c;break
        else:
            a=c
    return a
def lim(f,n=0,lmr=mm):
    s=1e-12;x1=n-s;x2=n+s
    if lmr==ll:
        ans=fx(f,x1)
    if lmr==mm:
        ans=(fx(f,x1)+fx(f,x2))/2
    if lmr==rr:
        ans=fx(f,x2)
    return ans
def xfx(f,x=0,n=100):
    for i in range(0,n):
        x=fx(f,x)
    return x
def sumx(f,x0=1,x1=100):
    ans=0
    for x in range(x0,x1+1):
        ans+=fx(f,x)
    return ans
def mpy(sss,cale=12):
    global ans
    ans=eval(sss)
    ans=cn_rn(ans,cale) if num(ans) else ans
    return ans