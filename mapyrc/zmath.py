import os,pypynum
# 在导入 mymath 之前设置不抑制 pypynum 输出
from math_adapter import set_global_suppress_pypynum_output
set_global_suppress_pypynum_output(suppress=False)

from mymath import *
# 在导入 mymath 之后再次确保不抑制 pypynum 输出
set_global_suppress_pypynum_output(suppress=False)

import readline as rdl
rdl.parse_and_bind("tab: complete")
_,scale=0,12
ti,ans,_line=_,_,lambda sss:'-'*29+sss
def mpy(sss,cale=12):
    ans=eval(sss)
    ans=cn_rn(ans,cale) if num(ans) else ans
    return ans
print(_line("-"*5))
print('赋值:set [x][=][1],退出:quit|exit\n清屏:clear,库函数:ma.[func]')
print(_line('--+'))
while ti<50:
    nbm=input('>>>')
    print(_line('--+'))
    if len(nbm)==0:
        continue
    elif nbm=="quit" or nbm=="exit":
        print('END');break
    elif nbm=="clear":
        os.system("clear");continue
    if not able_(nbm):
        print("[notice]:can't exec")
    elif nbm[:4]!="set ":
        _=mpy(nbm,scale);ti+=1
        print("(",ti,")--->",_)
    elif nbm[:4]=="set ":
        if len(nbm)<7: print("eg:set x=1");continue
        nbmm=[nbm[4],nbm[6:]]
        nbms="=".join(nbmm);ti+=1
        exec(nbms)
        print("(",ti,")--->赋值:",nbms)
    ans=_;print(_line('--+'))