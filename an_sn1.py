import sys
sys.path.append('mapyrc/')
import sympy as sm
import nyht as yh
get_ks,get_S=yh.get_ks,yh.get_S
sv=sys.argv
if len(sv)<2:
    f=input("a_n=n^")
else:
    f=sv[1];print(f"a_n=n^{f}")
al=int(f)
print("系数:",get_ks(al+1))
print("S_n=")
sn,j=get_S(al,True)
sn=sn.expand()
sm.pprint(sn)
if j==1:
    print("...")
print("[factor]")
if al>16:
    print("n²·(n+1)²...")
else:
    sm.pprint(sn.factor())