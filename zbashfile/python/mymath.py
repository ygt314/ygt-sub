'''
calculate for math
数学常用计算
(by YGT)
'''
import math as ma
import cmath as cm
pi=ma.pi;i=1j;deg='d';rad='r';e=ma.e
s2=2**0.5;phi=(5**0.5-1)/2;gama=0.577
def r_d(r):
    return r/pi*180
def d_r(d):
    return d/180*pi
def xsex(n,cale=12):
    '''尝试约化小数部分,但不处理整数
    支持复数,但只处理实部'''
    ans=n
    if type(n) != int:
        f='.'+str(cale)+'g'
        ans=eval(format(n,f))
    ans=ans.imag*1j if abs(n.real)<10**(-cale) else ans
    return ans
def cn_rn(c,cale=12):
    '''尝试得到实数'''
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
#双曲函数
sinh=cm.sinh;cosh=cm.cosh;tanh=cm.tanh
asinh=cm.asinh;acosh=cm.acosh;atanh=cm.atanh
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
sqrt=cm.sqrt;cbrt=lambda x:x**(1/3)
lg=cm.log10;ln=cm.log;log=cm.log
floor=ma.floor;ceil=ma.ceil
inf=10**12;s=1e-12
a,b,c,d=-7,-6,-5,-4
m,n=-3,-2
p,q=-1,1
x,y,z=2,3,4
u,v,w=5,6,7
from myfunc import *
def num(n):
    '''n is num?'''
    ans=False
    if type(n)==int or type(n)==float:
        ans=True
    elif type(n)==complex:
        ans=True
    return ans
#数列
def an(f,n=1):
    '''a_n=f(n),n∈N*'''
    return eval(f) if n>0 else 0
def dn(f,n=1):
    '''d_n=a_(n+1)-a_n,n∈N*'''
    return an(f,n)-an(f,n-1)
def sn(f,n=100):
    '''a_n=f(n):S_n,n∈N*'''
    ans=0
    for i in range(1,n+1):
        ans+=an(f,i)
    return ans
if __name__=="__main__":
    ems="e**(pi*i)+1"
    ans=eval(ems)
    print(ems,"=",ans)