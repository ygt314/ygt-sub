import os
from mymath import *
ti=0;scale=12
def mpy(sss,cale=12):
    global ans
    ans=eval(sss)
    ans=cn_rn(ans,cale) if num(ans) else ans
    return ans
print('------------------------------------------')
print('赋值:set [str],退出:quit|exit\n清屏:clear,库函数:ma.[func]')
print('--------------------------------------+')
while ti<50:
    nbm=input('>>>')
    print('--------------------------------------+')
    if len(nbm)==0:
        continue
    elif nbm=="quit" or nbm=="exit":
        print('END');break
    elif nbm=="clear":
        os.system("clear");continue
    if "__" in nbm:
        print("[notice]:can't import")
    elif nbm[:4]!="set ":
        aqwe=mpy(nbm,scale);ti+=1
        print("(",ti,")--->",aqwe)
    elif nbm[:4]=="set ":
        nbmm='mma.'+nbm[4:];ti+=1
        aqwe=exec(nbmm)
        print("(",ti,")--->赋值:",nbmm)
    print('--------------------------------------+')