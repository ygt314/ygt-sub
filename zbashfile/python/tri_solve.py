from mymath_real import *
sct="a";abc="A" #直接式结果(A),过程式结果(a)
#角度计算
deg="d";rad="r"
def tgt(dd=rad):
    '''直角90°(pi/2)'''
    ans=90 if dd==deg else mpy("pi/2",16)
    return ans
def modA(A,dd=rad):
    '''余角=直角-A'''
    return tgt(dd)-A
def sABC(dd=rad):
    '''三角形内角和(平角)
    A+B+C=180°(pi)'''
    ans=180 if dd==deg else mpy("pi",16)
    return ans
def conA(A,dd=rad):
    '''补角=平角-A'''
    return sABC(dd)-A
#三角形存在性
def AB_j(A,B,dd=rad):
    '''两角和小于平角'''
    dis=A+B-sABC(dd)
    ans=not abs(dis)<1e-9
    ans=False if A+B>sABC(dd) else ans
    return ans
def ABC_j(A,B,C,dd=rad):
    '''三角形内角和判断'''
    dis=sum([A,B,C])-sABC(dd)
    ans=abs(dis)<1e-9
    _s=[A,B,C,A,B,C]
    for i in range(3):
        ans=False if not AB_j(_s[i],_s[i+1],dd) else ans
    return ans
def abc_j(a,b,c):
    '''两边之和大于第三边'''
    _s=[a,b,c,a,b,c];abcj=True
    for i in range(3):
        dis=_s[i]+_s[i+1]-_s[i+2]
        abcj=False if abs(dis)<1e-9 else abcj
        abcj=False if _s[i]+_s[i+1]<_s[i+2] else abcj
    return abcj
#三角函数
def sa(ns,dd=rad):
    '''A->sinA'''
    return mpy(f"sin({ns},'{dd}')",16)
def ca(ns,dd=rad):
    '''A->cosA'''
    return mpy(f"cos({ns},'{dd}')",16)
def asa(ns,dd=rad,xx="+"):
    '''sinA->A
    xx is symbol of cosA(+/-)'''
    A=mpy(f"asin({ns},'{dd}')",16)
    A2=conA(A,dd)
    ans=A if xx=="+" else A2
    return ans
def aca(ns,dd=rad):
    '''cosA->A'''
    return mpy(f"acos({ns},'{dd}')",16)
def sa_ca(sa,xx="+"):
    '''sinA->cosA
    xx is symbol of cosA(+/-)'''
    ca=(1-sa*sa)**0.5
    ca=ca if xx=="+" else -ca
    return getrn(ca)
def ca_sa(ca):
    '''cosA->sinA'''
    sa=(1-ca*ca)**0.5
    return getrn(sa)
#定理求解
def AB_C(A,B,abc="A",dd=rad):
    '''三角形内角和定理A,B->C
    C=180°-A-B'''
    C=conA(A+B,dd)
    sinC=sa(A+B,dd)
    cosC=-ca(A+B,dd)
    scC=[getrn(sinC,11),getrn(cosC,11)]
    varC=getrn(C,11) if abc=="A" else scC
    return varC if ABC_j(A,B,C,dd) else 0
def abc_C(a,b,c,abc="A",dd=rad):
    '''余弦定理:a,b,c->C
    cosC=(a²+b²-c²)/(2ab)'''
    cosC=(a*a+b*b-c*c)/(2*a*b)
    C=aca(cosC,dd)
    sinC=ca_sa(cosC)
    scC=[getrn(sinC,11),getrn(cosC,11)]
    varC=getrn(C,11) if abc=="A" else scC
    return varC
def abC_c(a,b,C,abc="A",dd=rad):
    '''余弦定理:a,b,C->c
    c²=a²+b²-2ab*cosC'''
    c2=a*a+b*b-2*a*b*ca(C,dd)
    c=c2**0.5
    varc=c if abc=="A" else c2
    return getrn(varc,11)
def abA_B(a,b,A,abc="A",dd=rad,xx="+"):
    '''正弦定理:a,b,A->B
    sinB=b/a*sinA'''
    sinB=b*sa(A,dd)/a
    B=asa(sinB,dd,xx)
    cosB=sa_ca(sinB,xx)
    scB=[getrn(sinB,11),getrn(cosB,11)]
    varB=getrn(B,11) if abc=="A" else scB
    return varB
def ABa_b(A,B,a,abc="A",dd=rad):
    '''正弦定理:A,B,a->b
    b=sinB/sinA*a'''
    b=a*sa(B,dd)/sa(A,dd)
    b2=b*b
    varb=b if abc=="A" else b2
    return getrn(varB,11)
def ab_c(ab,AB,abc="A",dd=rad):
    '''射影定理:[a,b],[A,B]->c
    c=a*cosB+b*cosA'''
    a,b=ab
    A,B=AB
    c=a*ca(B,dd)+b*ca(A,dd)
    c2=c*c
    varc=c if abc=="A" else c2
    return varc
#三角形分类求解
def abc_ABC(a,b,c,abc="A",dd=rad):
    '''SSS(三边对三角)'''
    A=abc_C(b,c,a,abc,dd)
    B=abc_C(c,a,b,abc,dd)
    C=abc_C(a,b,c,abc,dd)
    return [[A,B,C],[a,b,c]] if abc_j(a,b,c) else []
def abC_ABc(a,b,C,abc="A",dd=rad):
    '''SAS(两边夹一角)'''
    c0=abC_c(a,b,C,'A',dd)
    c=abC_c(a,b,C,abc,dd)
    A=abc_C(b,c0,a,abc,dd)
    B=abc_C(c0,a,b,abc,dd)
    return [[A,B,C],[a,b,c]]
def abA_BCc(a,b,A,abc="A",dd=rad,xx="+"):
    '''SSA(两边对一角)'''
    B0=abA_B(a,b,A,'A',dd,xx)
    B=abA_B(a,b,A,abc,dd,xx)
    C=AB_C(A,B0,abc,dd)
    c=ab_c([a,b],[A,B0],abc,dd)
    return [[A,B,C],[a,b,c]] if ABC_j(A,B0,C,dd) else []
def ABc_Cab(A,B,c,abc="A",dd=rad):
    '''ASA(两角夹一边)'''
    C0=AB_C(A,B,'A',dd)[0]
    C=AB_C(A,B,abc,dd)[0]
    a=ABa_b(C0,B,c,abc,dd)
    b=ABa_b(C0,A,a,abc,dd)
    return [[A,B,C],[a,b,c]] if ABC_j(A,B,C0,dd) else []
def ABa_Cbc(A,B,a,abc="A",dd=rad):
    '''AAS(两角对一边)'''
    C0=AB_C(A,B,'A',dd)
    C=AB_C(A,B,abc,dd)
    b=ABa_b(A,B,a,abc,dd)
    c=ABa_b(A,C0,a,abc,dd)
    return [[A,B,C],[a,b,c]] if ABC_j(A,B,C0,dd) else []
def ABC_abc(A,B,abc="A",dd=rad):
    '''AAA(三角对三边)
    假设a=1'''
    C0=AB_C(A,B,'A',dd)
    C=AB_C(A,B,abc,dd)
    b=ABa_b(A,B,1,abc,dd)
    c=ABa_b(A,C0,1,abc,dd)
    return [[A,B,C],[1,b,c]] if ABC_j(A,B,C0,dd) else []
#周长
def cabc(a,b,c):
    return sum([a,b,c])
def sabc(a,b,c):
    return cabc(a,b,c)/2
#面积
def qinjz(a,b,c):
    '''秦九昭公式
    S=1/2*√(a²b²-(a²+b²-c²)²/4)'''
    ah2=a*a*b*b-(a*a+b*b-c*c)**2/4
    area=ah2**0.5/2
    return getrn(area,10)
def helen(a,b,c):
    '''海伦公式
    S=1/2*√(s(s-a)(s-b)(s-c))'''
    s=sabc(a,b,c)
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return getrn(area,10)
def sabsC(a,b,C,dd=rad):
    '''边角面积公式
    S=1/2*ab*sinC'''
    return getrn(a*b*sa(C,dd)/2)
#中线,高线,角平分线
def ma(a,b,c):
    '''中线长公式
    m_a=1/2*√(2a²+2c²-a²)'''
    m2=2*b*b+2*c*c-a*a
    return getrn(m2**0.5/2)
def ha(a,b,c,abc="A"):
    '''秦九昭公式的高
    h_a=√(b²-(a²+b²-c²)²/(2a)²)'''
    a2,b2,c2=a*a,b*b,c*c
    ha2=b2-(a2+b2-c2)**2/(a2*4)
    ha=ha2**0.5
    varh=ha if abc=="A" else ha2
    return getrn(varh)
def la(a,b,c):
    '''角平分线长
    l_a=√(bc[(b+c)²-a²])/(b+c)'''
    lab2=b*c*((b+c)**2-a*a)
    return getrn((lab2)**0.5/(b+c))
def mabc(a,b,c):
    '''中线长[ma,mb,mc]'''
    _s=[a,b,c,a,b,c]
    return [ma(_s[i],_s[i+1],_s[i+2]) for i in range(3)]
def habc(a,b,c):
    '''高线长[ha,hb,hc]'''
    _s=[a,b,c,a,b,c]
    return [ha(_s[i],_s[i+1],_s[i+2]) for i in range(3)]
def labc(a,b,c):
    '''角平分线长[la,lb,lc]'''
    _s=[a,b,c,a,b,c]
    return [la(_s[i],_s[i+1],_s[i+2]) for i in range(3)]
#外接圆,内切圆
def Rabc(a,b,c):
    '''外接圆半径
    R=abc/(4s)'''
    s4=s(a,b,c)*4
    return getrn(a*b*c/s4)
def rabc(a,b,c):
    '''内切圆半径
    r=S/s=√((s-a)(s-b)(s-c)/s)'''
    s=sabc(a,b,c)
    tabc=(s-a)*(s-b)*(s-c)
    return getrn((tabc/s)**0.5)
if __name__=="__main__":
    a,b,c=3,4,5;print("△ABC,a=3,b=4,c=5")
    rads=abc_ABC(a,b,c);A,B,C=rads[0]
    degs=abc_ABC(a,b,c,"A","d");Ad,Bd,Cd=degs[0]
    print("存在性:",abc_j(a,b,c))
    print("A=",A,"=",Ad,"°")
    print("B=",B,"=",Bd,"°")
    print("C=",C,"=",Cd,"°")
    print("Length=",labc(3,4,5))
    print("s=",sabc(3,4,5))
    print("Area=",helen(3,4,5))