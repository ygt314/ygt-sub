from sys import argv
def cont_sqrt(a,b):
    if b==0:
        return a
    else:
        return (a+cont_sqrt(b,0))**0.5
def nums(ss):
    if "/" in ss:
        s=ss.split("/")
        ans=float(s[0])/float(s[1])
    else:
        ans=float(ss)
    return ans
# 定义序列
seqs=[0]
if len(argv)>1:
    seqs=argv[1].split(",")
# 计算序列
result=nums(seqs[-1])**0.5
for i in range(len(seqs)-2,-1,-1):
    result=cont_sqrt(nums(seqs[i]),result)
print(result)