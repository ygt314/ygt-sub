'''
calculate for real number
实数计算
(by YGT)
'''
import mymath as mm
def getrn(c,cale=12):
    '''强制得到实数'''
    n=mm.cn_rn(c,cale)
    return n.real
def mpy(sss,cale=16):
    ans=mm.mpy(sss,cale)
    return getrn(ans)
if __name__=="__main__":
    ans=mpy("i")
    print("i","=",ans)