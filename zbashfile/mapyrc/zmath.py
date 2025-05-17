import os
from mymath import *
ti=0;scale=12
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
    i=1j
    if nbm[:2]=="__" or nbm[4:6]=="__":
        print("[notice]:can't import")
    elif nbm[:4]!="set ":
        aqwe=mpy(nbm,scale);ti+=1
        print("(",ti,")--->",aqwe)
    elif nbm[:4]=="set ":
        nbmm=nbm[4:];ti+=1
        aqwe=exec(nbmm)
        print("(",ti,")--->赋值:",nbmm)
    print('--------------------------------------+')