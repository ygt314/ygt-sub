import os
from mymath import *
ti=0;scale=12
print('------------------------------------------')
print('赋值:set [str],退出:quit|exit\n清屏:clear,库函数:ma.[func]')
print('--------------------------------------+')
while ti<50:
    nbm=input('>>>')
    print('--------------------------------------+')
    if nbm=="quit" or nbm=="exit":
        print('END')
        break
    elif nbm=="clear":
        os.system("clear")
    i=1j
#    for str1 in range(0,len(nbm)):
#        nbm=nbm.replace('i','*1j')
    if nbm!="quit" and nbm!="clear" and nbm!="":
        if nbm[:4]!="set ":
            aqwe=mpy(nbm,scale);ti+=1
            print("(",ti,")--->",aqwe)
        elif nbm[:4]=="set ":
            nbmm=nbm[4:];ti+=1
            aqwe=exec(nbmm)
            print("(",ti,")--->赋值:",nbmm)
        print('--------------------------------------+')