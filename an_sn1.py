import sys
sys.path.append('mapyrc/')
import nyht as yh
import sympy as sm
def get_k(n,m,k):
    ron=yh.ros(n,m);ans=0
    for i in range(0,n):
        ans+=ron[i]*ks[i]
    return -ans/ron[n]
ss=sm.S;n=ss("n")
sv=sys.argv
if len(sv)<2:
    f=input("a_n=n^")
else:
    f=sv[1];print(f"a_n=n^{f}")
al=int(f)
nl=al+1;ks=[1/ss(nl)]
for i in range(0,al):
    ks+=[get_k(i+1,nl,ks)]
print("系数:",ks)
print("S_n=");sn=0;j=0
for i in range(0,nl):
    if i>40:
        j=1;break
    sn+=ks[i]*n**(nl-i)
sn=sm.expand(sn)
sm.pprint(sn)
if j==1:
    print("...")
print("[factor]")
if al>16:
    print("n²·(n+1)²...")
else:
    sm.pprint(sn.factor())