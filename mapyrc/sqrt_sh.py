import sys,sq_cal
sv=sys.argv;sqb=sq_cal.sq_bi
a=input("a=") if len(sv)==1 else sv[1]
if len(a)>20:
    print("warning:a is long")
a=int(float(a))
aj=1 if a<0 else 0
a=abs(a);ss=len(str(a))
if ss>100:
    print("warning:a:len=",ss,":t=",(ss-100)//67,(ss-100)//56)
sq0=sqb(a)
ans=str(sq0);ss=len(ans)
s=input("scale=") if len(sv)<=2 else sv[2]
s=6 if len(s)==0 else int(s)
s=1474-ss if s>1474-ss else s
if s==1474-ss:
    print("warring:s_max=1474")
if s>0:
    f,i="",sq0
    nbc=20*i
    nbb,nba=nbc,a-i*i
    for k in range(1,s+1):
        nba*=100
        nbb-=1
        for j in range(0,10):
            nbb+=2
            nba-=nbb
            if nba<=0:
                nba+=nbb
                nbb-=2
                f+=str(j);break
            elif j==9:
                print("error:j>9")
        nbc=nbc*10+j*20
        nbb=nbc
    ans+="."+f
if aj==1:
    print(ans+"i")
else:
    print(ans)