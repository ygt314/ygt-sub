from mymath import *
import sys
sv=sys.argv
nbm=sv[1];scale=12
if len(sv)==3:
    scale=int(sv[2])
if nbm=="quit" or nbm=="exit":
    print('END')
elif nbm=="clear":
    print('clear')
if nbm!="quit" and nbm!="clear" and nbm!="":
    if nbm[:4]!="set ":
        aqwe=mpy(nbm,scale)
        print(aqwe)
    elif nbm[:4]=="set ":
        nbmm=nbm[4:]
        print("赋值:"+nbmm)