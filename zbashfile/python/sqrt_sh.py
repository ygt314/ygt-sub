import sys
sv=sys.argv
a=input("a=") if len(sv)==1 else sv[1]
a=int(float(a))
aj=1 if a<0 else 0
a=abs(a)
ss=len(str(a))
if ss>14 and ss<30:
    print("warring:a:len=",ss,":t=",5*2**(ss-15),9*2**(ss-15))
if ss>17:
    print("error:a:too large");exit()
s2=(ss-1)//2
b=10**s2 if ss>1 else 0
for i in range(b,a+1):
    if i*i<=a:
        sq0=i
    else:
        break
ans=str(sq0)
ss=len(ans)
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