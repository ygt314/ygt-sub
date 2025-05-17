from mymath_real import *
sct="a";abc="A";deg="d";rad="r"
def sa(ns,dd=rad):
    return mpy(f"sin({ns},'{dd}')",16)
def ca(ns,dd=rad):
    return mpy(f"cos({ns},'{dd}')",16)
def asa(ns,dd=rad,xx="+"):
    r=mpy(f"asin({ns},'{dd}')",16)
    tgt=90 if dd==deg else mpy("pi/2",16)
    r2=r+tgt
    ans=r if xx=="+" else r2
    return ans
def aca(ns,dd=rad):
    return mpy(f"acos({ns},'{dd}')",16)
def sa_ca(sa,xx="+"):
    ca=(1-sa*sa)**0.5
    ca=ca if xx=="+" else -ca
    return getrn(ca)
def ca_sa(ca):
    sa=(1-ca*ca)**0.5
    return getrn(sa)
def sABC(dd=rad):
    ans=180 if dd==deg else mpy("pi",16)
    return ans
def abc_C(a,b,c,abc="A",dd=rad):
    cosC=(a*a+b*b-c*c)/(2*a*b)
    varC=aca(cosC,dd) if abc=="A" else cosC
    return getrn(varC,11)
def abA_B(a,b,A,abc="A",dd=rad,xx="+"):
    sinB=b*sa(A,dd)/a
    varB=asa(sinB,dd,xx) if abc=="A" else sinB
    return getrn(varB,11)
def abc_ABC(a,b,c,abc="A",dd=rad):
    A=abc_C(b,c,a,abc,dd)
    B=abc_C(c,a,b,abc,dd)
    C=abc_C(a,b,c,abc,dd)
    return [A,B,C]
def abC_ABc(a,b,C,abc="A",dd=rad):
    c=(a*a+b*b-2*a*b*ca(C,dd))**0.5
    A=abc_C(b,c,a,abc,dd)
    B=abc_C(c,a,b,abc,dd)
    return [A,B,getrn(c)]
def abA_BCc(a,b,A,abc="A",dd=rad,xx="+"):
    B=abA_B(a,b,A,abc,dd,xx)
    C=sABC(dd)-A-B
    c=a*ca(B,dd)+b*ca(A,dd)
    return [B,getrn(C),getrn(c)]
def ABc_Cab(A,B,c,abc="A",dd=rad):
    C=sABC(dd)-A-B
    a=c*sa(A,dd)/sa(C,dd)
    b=c*sa(B,dd)/sa(C,dd)
    return [getrn(C),getrn(a),getrn(b)]
def ABa_Cbc(A,B,a,abc="A",dd=rad):
    C=sABC(dd)-A-B
    b=a*sa(B,dd)/sa(A,dd)
    c=a*sa(C,dd)/sa(A,dd)
    return [getrn(C),getrn(b),getrn(c)]
def ABC_abc(A,B,C,abc="A",dd=rad):
    b=sa(B,dd)/sa(A,dd)
    c=sa(C,dd)/sa(A,dd)
    return [1,getrn(b),getrn(c)]
def labc(a,b,c):
    return getrn(a+b+c)
def sabc(a,b,c):
    return getrn((a+b+c)/2)
def helen(a,b,c):
    s=sabc(a,b,c);area=(s*(s-a)*(s-b)*(s-c))**0.5
    return getrn(area,10)
def sabsC(a,b,C,dd=rad):
    return getrn(a*b*sa(C,dd)/2)
if __name__=="__main__":
    a,b,c=3,4,5;print("△ABC,a=3,b=4,c=5")
    rads=abc_ABC(a,b,c);A,B,C=rads
    degs=abc_ABC(a,b,c,"A","d");Ad,Bd,Cd=degs
    print("A=",A,"=",Ad,"°")
    print("B=",B,"=",Bd,"°")
    print("C=",C,"=",Cd,"°")
    print("Length=",labc(3,4,5))
    print("s=",sabc(3,4,5))
    print("Area=",helen(3,4,5))