from mymath import *
import sys
sv=sys.argv;nbm=sv[1];scale=12
def mpy(sss,cale=12):
    global ans
    ans=eval(sss)
    ans=cn_rn(ans,cale) if num(ans) else ans
    return ans
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
elif "__" in nbm:
    print("[notice]:can't import");exit()
if nbm[:4]!="set ":
    aqwe=mpy(nbm,scale)
    print(aqwe)
elif nbm[:4]=="set ":
    nbmm=nbm[4:]
    print("赋值:"+nbmm)