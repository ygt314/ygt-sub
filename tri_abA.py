from sys import path
path.append('mapyrc/')
from tri_solve import *
a,b,A=input("a,b,A°:>").split(",")
print(f"△ABC,a={a},b={b},A={A}°")
a,b,A=float(a),float(b),float(A)
if a<b*sa(A,deg):
    print("此三角形无解");exit()
B,C,c=abA_BCc(a,b,A,"A",deg)
sB2,sC2,sc2,sl2,ss2,sa2="","","","","",""
if a<b and abs(a-b*sa(A,deg))>1e-10:
    print("此三角形有两个解")
    sol2d=["B2","C2"];sol2b=["c2","Length2","s2","Area2"]
    sol2=abA_BCc(a,b,A,"A",deg,"-")
    sB2,sC2=[f"or {sol2d[i]}={sol2[i]}°" for i in [0,1]]
    sol2i=[sol2[2]]+[labc(a,b,c),sabc(a,b,c),helen(a,b,c)]
    sc2,sl2,ss2,sa2=[f"or {sol2b[i]}={sol2i[i]}" for i in range(0,4)]
else:
    print("此三角形仅有一个解")
print(f"B1={B}°",sB2)
print(f"C1={C}°",sC2)
print(f"c1={c}",sc2)
print(f"Length1={labc(a,b,c)}",sl2)
print(f"s1={sabc(a,b,c)}",ss2)
print(f"Area1={helen(a,b,c)}",sa2)