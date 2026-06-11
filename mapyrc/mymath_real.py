'''
calculate for real number
实数计算
(by YGT)
'''
from mymath import *
def getrn(c,cale=12):
    '''强制得到实数'''
    n=cn_rn(c,cale)
    return n.real
def getfs(c,cale=12):
    '''获取分数形式'''
    a=getrn(c,15)
    return confs(a)
def mmpy(sss,cale=12):
    global ans
    ans=eval(sss)
    ans=getrn(ans,cale) if num(ans) else ans
    return ans
def mpy(sss,cale=16):
    ans=mmpy(sss,cale)
    return getrn(ans)
if __name__=="__main__":
    ans=mpy("pi")
    print("pi","=",ans)
    print("=",confs(ans))