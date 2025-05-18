import sympy as sm
import sys
sv=sys.argv
if len(sv)<2:
    f=input("S_n=")
else:
    f=sv[1]
func=sm.S(f)
func1=func.subs("n","n-1")
print("a_1=S_1=")
f1=func.subs("n",1);sm.pprint(f1)
print("if n>=2,a_n=S_n-S_(n-1)=")
an=sm.simplify(func-func1);sm.pprint(an)
print("(if n=1,");a1=an.subs("n",1)
aeq=sm.Eq(a1,f1);ans=sm.solve(aeq)
if ans!=[]:
    sm.pprint(ans);print("it's equal to a_1)")
elif a1==f1:
    print("it's equal to a_1)")
else:
    print("it's not equal to a_1)")
print("[expand]")
dfn=sm.expand(an);sm.pprint(dfn)
print("[factor]")
ffn=sm.factor(dfn);sm.pprint(ffn)