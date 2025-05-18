from chempy import balance_stoichiometry
import sys
sv=sys.argv
def nege(n):
    if j==0:
        nm=str(n)
    else:
        nm="" if n<0 else "+"
        nm+=str(n)
    return nm
#读取反应物和生成物
if len(sv)>2:
    rets=sv[1].split(",")
    prts=sv[2].split(",")
else:
    print("use:che_ba.py [rets] [prts]");exit()
eq,eqfh="",'='
# 调用balance_stoichiometry函数进行配平
eqs=balance_stoichiometry(rets, prts)
eqls=eqs[0];eqrs=eqs[1];j=0
for ret in rets:
    sth=nege(eqls[ret])+ret
    eq+=sth;j=1
eql=eq;eq='';j=0
for prt in prts:
    sth=nege(eqrs[prt])+prt
    eq+=sth;j=1
eqr=eq;eq=eql+eqfh+eqr
print(eq)