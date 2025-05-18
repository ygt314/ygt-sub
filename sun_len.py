from sys import path
path.append('mapyrc/')
from mymath import *
from os import system
def n_s(d):
    s="N" if d>0.01 else " "
    return "S" if d<-0.01 else s
def e_w(d):
    s="E" if d>0.01 else " "
    return "W" if d<-0.01 else s
def d_dms(d):
    di=int(d);df=abs(d-di);hh=df*60
    hi=int(hh);hf=hh-hi;si=format(hf*60,".2f")
    dms=str(di)+"°"+str(hi)+"'"+si+"''"
    return dms
def h_hms(h):
    hi=int(h);hf=abs(h-hi);mm=hf*60
    mi=int(mm);mf=mm-mi;si=format(mf*60,".2f")
    hms=str(hi)+"h"+str(mi)+"m"+si+"s"
    return hms
def prwd(s):
    wd=dhom if s=="h" else dsch;wds=str(wd)+"°N"
    dkey="在家" if s=="h" else "在校";system("clear")
    print(dkey+"纬度:",wds,end="=");print(d_dms(wd)+"N")
    return wd
def now_sun():
    nowj=180-(nows%86400)/240
    print("太阳直射点:(",d_dms(abs(nowc)),end=n_s(nowc)+",")
    print(d_dms(abs(nowj))+e_w(nowj)+")"+" "*6,end='\r')
from time import sleep
from datetime import datetime
dt=datetime;now=dt.now;nowt=now()
da_s=86400
ye_s=da_s*365.2422
def sunlen(nows):
    prds=(nows-sprs)/ye_s if nows<sums else 0.5+(nows-auts)/ye_s
    dhd=d_r(prds*360);cwtg=sin(dhd)*tan(dhg)
    sun_len=12+24*asin(tan(dwd,deg)*cwtg)/pi
    return sun_len.real
jstr=input("地点纬度:")
dhom,dsch=25.599075,25.791936
dhg=d_r(23.5)
dwd=dhom
if jstr=="":
    prwd("h")
elif jstr=="h" or jstr=="s":
    dwd=prwd(jstr)
else:
    dwd=mpy(jstr)
nowy=nowt.year;nowm=nowt.month;nowd=nowt.day
nows0=dt(nowy,nowm,nowd).timestamp()
sprs=dt(nowy,3,21,14,10).timestamp()
sums=dt(nowy,6,22,12).timestamp()
auts=dt(nowy,9,23,9,50).timestamp()
sun_len=sunlen(nows0)/da_s
print("计算昼长中…",end="\r")
for i in range(1,da_s+1):
    sun_len+=sunlen(nows0+i)/da_s
print("今天昼长:",format(sun_len,"f"),"h",end="=")
print(h_hms(sun_len))
while jstr!="quit":
    nows=now().timestamp()
    nowhs=360*(nows-sprs)/ye_s
    nowha=180+360*(nows-auts)/ye_s
    nowh=nowhs if nows<sums else nowha
    nowc=cn_rn(atan(sin(nowh,deg)*tan(dhg),deg))
    now_sun();sleep(0.16)
