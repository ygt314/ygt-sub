import sys
import sympy as sm
from sympy.abc import a,b,r
r2=r*r;sv=sys.argv
def syn(n):
    return str(n) if n<0 else "+"+str(n)
def syn_a(n):
    ans=syn(n)
    return "" if n==0 else ans
def syn_t(n):
    ans=syn(n)
    return ans[0] if abs(n)==1 else ans
def rsv(var):
    return [sm.S(i) for i in var.split(",")]
def get_eq(x,y):
    x_2=(x-a)**2
    y_2=(y-b)**2
    return sm.Eq(x_2+y_2,r2)
def get_eq0(x,y):
    x_2="("+str(x)+"-a)²"
    y_2="("+str(y)+"-b)²"
    return x_2+"+"+y_2+"=r²"
def get_eq1(x,y):
    sxy=syn_a(x*x+y*y)
    ndx=syn_t(-2*x)
    ndy=syn_t(-2*y)
    return "a²+b²"+ndx+"a"+ndy+"b"+sxy+"=r²"
def get_eq3(a,b,rr):
    x_2="(x"+syn_a(-a)+")²"
    y_2="(y"+syn_a(-b)+")²"
    return x_2+"+"+y_2+"="+str(rr)
A=(5,1);B=(7,-3);C=(2,-8)
if len(sv)==4:
    A=rsv(sv[1])
    B=rsv(sv[2])
    C=rsv(sv[3])
eq1=get_eq(A[0],A[1])
eq2=get_eq(B[0],B[1])
eq3=get_eq(C[0],C[1])
print("Set to (x-a)²+(y-b)²=r².")
print("let three points into it",",get")
print("┌"+get_eq0(A[0],A[1]))
print("┤"+get_eq0(B[0],B[1]))
print("└"+get_eq0(C[0],C[1]))
print("It is")
print("┌"+get_eq1(A[0],A[1]))
print("┤"+get_eq1(B[0],B[1]))
print("└"+get_eq1(C[0],C[1]))
aa,bb,rr=sm.solve([eq1,eq2,eq3],a,b,r2)[0]
print("Solved,")
print("a=",aa,",b=",bb,",r²=",rr)
print("We can get,")
print(get_eq3(aa,bb,rr))