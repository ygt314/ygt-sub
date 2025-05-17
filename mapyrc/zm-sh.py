from mymath import *
import sys
sv=sys.argv
nbm=sv[1];scale=12
if len(sv)==3:
    scale=int(sv[2])
elif len(sv)==1:
    print("use:zm-sh.py [expr] [scale=12]");exit()
if nbm=="quit" or nbm=="exit":
    print('END')
elif nbm=="clear":
    print('clear')
if nbm=="quit" or nbm=="clear":
    exit()
elif nbm[:2]=="__" or nbm[4:6]=="__":
    print("[notice]:can't import");exit()
if nbm[:4]!="set ":
    aqwe=mpy(nbm,scale)
    print(aqwe)
elif nbm[:4]=="set ":
    nbmm=nbm[4:]
    print("赋值:"+nbmm)