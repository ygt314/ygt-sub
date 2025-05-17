'''n阶等差数列求和系数求解'''
def nj(n):
    '''(-1)^n'''
    return -1 if n%2==0 else 1
def cmn(m,n):
    '''C(m,n)'''
    a=m if m<n else n
    b=n if m<n else m
    h,g=1,1
    for i in range(0,int(a)):
        	h=h*(b-i);g=g*(i+1)
    return h//g
def dmn(m,n,t):
    '''(m,n) is (line,row)
    m,n begain from 0
    t is total of line'''
    d=t-m
    return 0 if m>n else cmn(n-m+1,d)*nj(n-m+1)
def lis(n,m):
    '''n is line num(natural)
    m is total of line'''
    d=m-n;lin=[0]*n
    for i in range(0,d):
        lin+=[cmn(i+1,d)*nj(i+1)]
    return lin
def ros(n,m):
    '''n is row num(natural)
    m is total of line'''
    row=[]
    for i in range(0,n):
        row+=[dmn(i,n,m)]
    return row+[dmn(n,n,m)]

def dns(n):
    '''n is line num
    (0,1,2...)'''
    dnm=[]
    for i in range(0,n):
        dnm+=[lis(i,n)]
    return dnm
if __name__=='__main__':
    total,line,row=8,3,3
    print("total:",total,",line:",line+1,",row:",row+1)
    print(dns(total))
    print(lis(line,total))
    print(dmn(line,row,total))
    print(ros(row,total))