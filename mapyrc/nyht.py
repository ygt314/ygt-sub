'''n阶等差数列求和'''
import sympy as sm
_ss=sm.S
def nj(n):
    '''(-1)^n'''
    return -1 if n%2==0 else 1
def cmn(m,n):
    '''C(m,n)'''
    a=m if m<n else n
    b=n if m<n else m
    h,g,c=1,1,b-a
    for i in range(int(c if c<a else a)):
        	h*=(b-i);g*=(i+1)
    return h//g
#差分计算
def dmn(m,n,t):
    '''差分计算
    (m,n) is (line,row)
    m,n begain from 0
    t is total of line'''
    d=t-m
    return 0 if m>n else cmn(n-m+1,d)*nj(n-m+1)
def lis(n,m):
    '''生成行差分表
    n is line num(natural)
    m is total of line'''
    d=m-n;lin=[0]*n
    for i in range(d):
        lin+=[cmn(i+1,d)*nj(i+1)]
    return lin
def ros(n,m):
    '''生成列差分表
    n is row num(natural)
    m is total of line'''
    return [dmn(i,n,m) for i in range(n+1)]
def dns(n):
    '''差分表
    n is line num
    (0,1,2...)'''
    return [lis(i,n) for i in range(n)]
#系数计算
def _get_k(n,m,ks):
    '''辅助计算系数'''
    ron=ros(n,m);ans=0
    for i in range(0,n):
        ans+=ron[i]*ks[i]
    return -ans/ron[n]
def get_k(n=1,m=1):
    '''a_n="n"^(m-1),S_n
    降幂排列的第n项系数'''
    if n<=1: return 1/_ss(m)
    return (get_ks(m,n))[n-1]
def get_ks(m=1,_k=0):
    '''a_n=n^(m-1),S_n
    降幂排列的系数
    _k:截断运算的位置'''
    ks,kj=[1/_ss(m)],0<_k<m
    for i in range(1,m):
        if kj and i==_k: break
        ks+=[_get_k(i,m,ks)]
    return ks
#求差
def get_d(k,l_j=False):
    '''d_n=a_n-a_(n-1)'''
    dn,n,m=0,_ss('n'),k
    if l_j: return lis(k)
    for i in lis(0,k):
        m-=1
        dn+=i*n**m
    return dn
def get_dn(ks):
    sn,j=0,len(ks)
    for i in ks:
        j-=1
        sn+=get_d(j)*i
    return sn
#求和
def get_s(kk,l_j=False):
    '''a_n=n^kk,S_n=?l_j:list'''
    sn,k,j,n=0,kk+1,0,_ss('n')
    if l_j: return get_ks(k)
    for i in get_ks(k):
        sn+=i*n**k;k-=1
    return sn
def get_sn(ks):
    '''ks:降幂排列的a_n系数列表'''
    sn,j=0,len(ks)
    for i in ks:
        j-=1
        sn+=get_s(j)*i
    return sn
def get_S(kk,lim=False):
    '''a_n=n^kk,S_n=?,limit scale.'''
    if not lim: return get_s(kk),0
    sn,k=0,kk+1
    ks,n=get_ks(k),_ss('n')
    for i in range(k):
        if i>40: break
        sn+=ks[i]*n**(k-i)
    return sn,1
def get_Sn(kk,lim=False):
    '''a_n=n^kk,S_n=...'''
    sn,i=get_S(kk,lim)
    j='' if i==0 else '...'
    return f"{sn} {j}"
if __name__=='__main__':
    total,line,row=8,3,3
    print("total:",total,",line:",line+1,",row:",row+1)
    print(dns(total))
    print(lis(line,total))
    print(dmn(line,row,total))
    print(ros(row,total))