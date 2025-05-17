'''
calculate sqrt(n)
'''
def sq_n(n=1):
    x=abs(n)
    for i in range(0,x+1):
        if i*i<=x:
            a=i;break
    return a
def sq_n1(n=1):
    x=abs(n);s=(len(str(x))-1)//2;a=0
    for i in range(10**s,x+1):
        if i*i<=x:
            a=i;break
    return a
def sq_bi(n=1):
    x=abs(n);s=(len(str(x))-1)//2
    a,b=10**s if x>0 else 0,x+1
    while b-a>1:
        c=(a+b)//2
        if c*c>x:
            b=c
        elif c*c==x:
            a=c;break
        else:
            a=c
    return a
def sq_nt(n=1):
    x=abs(n);s=(len(str(x))-1)//2;a=10**s
    for i in range(0,10^4):
        b=a;a=(b+x/b)//2;
        if a==b or a==0:
            break
    return a