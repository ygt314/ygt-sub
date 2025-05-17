"""
正面弹性碰撞(Frontal elastic collision)
m1v1+m2v2=m1v11+m2v21
m1v1^2+m2v2^2=m1v11^2+m2v21^2
结论(Result)
v1_final=(m1-m2)/(m1+m2)*v1+2m2/(m1+m2)*v2
v2_final=2m1/(m1+m2)*v1+(m2-m1)/(m1+m2)*v2
一般正面碰撞(General frontal collision)
m1v1+m2v2=m1v11+m2v21
m1v1^2+m2v2^2>=m1v11^2+m2v21^2
elastic recovery:e=(v21-v11)/(v1-v2)
结论(Result)
v1_final=(m1v1+m2v2+m2*e*(v2-v1))/(m1+m2)
v2_final=(m1v1+m2v2+m1*e*(v1-v2))/(m1+m2)
"""
def mp_ab(vss,vp=2):
    '''
mp_ab:collidability
mp_ab测试可碰撞性
vss:[v1,v2]
vss为两物体速度
vp: m_n location is positive direction
vp指定某个物体的位置为正方向'''
    vz=vss[0] if vp==1 else vss[1]
    vf=vss[1] if vp==1 else vss[0]
    if vz>=vf:
        return False
    else:
        return True
def coll(mss,vss,vp=0):
    '''
mss:[m1,m2] mass
mss指定质量
vss:[v1,v2] velocity
vss指定速度
vp:positive direction
vp指定正方向用于判断可碰撞性
(vp=0不指定方向，跳过判断)'''
    if len(mss) != 2 or len(vss) != 2:
        raise ValueError("There aren't two m(or v)")
    if vp not in [0,1,2]:
        raise ValueError("vp must is 0,1 or 2")
    m1,m2=mss[0],mss[1]
    v1,v2=vss[0],vss[1]
    av1=(m1-m2)*v1+2*m2*v2
    v11=av1/(m1+m2)
    av2=(m2-m1)*v2+2*m1*v1
    v21=av2/(m1+m2)
    if vp==0:
        return [v11,v21]
    elif mp_ab(vss,vp):
        return [v11,v21]
    else:
        return [v1,v2]
def coll0(mss,vss,vp=0):
    '''perfectly inelastic collision
完全非弹性碰撞，用法同coll'''
    if len(mss) != 2 or len(vss) != 2:
        raise ValueError("There aren't two m(or v)")
    if vp not in [0,1,2]:
        raise ValueError("vp must is 0,1 or 2")
    m1,m2=mss[0],mss[1]
    v1,v2=vss[0],vss[1]
    av1=m1*v1+m2*v2
    v1=av1/(m1+m2)
    if vp==0:
        return [v11,v21]
    elif mp_ab(vss,vp):
        return [v11,v21]
    else:
        return [v1,v2]
def e_coll(mss,vss,e=1,vp=0):
    '''e:elastic recovery
e指定恢复系数，其它同coll'''
    if len(mss) != 2 or len(vss) != 2:
        raise ValueError("There aren't two m(or v)")
    if vp not in [0,1,2]:
        raise ValueError("vp isn't 0,1 or 2")
    if e<0 or e>1:
        raise ValueError("e not belong to [0,1]")
    m1,m2=mss[0],mss[1]
    v1,v2=vss[0],vss[1]
    av1=m1*v1+m2*v2+m2*e*(v2-v1)
    v1=av1/(m1+m2)
    av2=m1*v1+m2*v2+m2*e*(v1-v2)
    v2=av2/(m1+m2)
    if vp==0:
        return [v11,v21]
    elif mp_ab(vss,vp):
        return [v11,v21]
    else:
        return [v1,v2]
if __name__=="__main__":
    mm,vv,op=[2,6],[8,9],1
    print("mass",mm)
    print(f"Set m{op} is positive.")
    print("[start]");print("velocity",vv)
    print("Will coll?");print(mp_ab(vv,op))
    print("[end]")
    print("velocity",coll(mm,vv,op))