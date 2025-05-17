i=0
print("欢迎来到v1.55版的一元二次方程求解工具")
print("maker:Yuan Great(CN)\nfinishtime:2024/03/30 16:03")
while i<10:
    i+=1
    print("─────────────────────────┐")
    print("请键入方程  ax²+bx+c=0 三个参数 a b c\n    输入数字或表达式")
    print("─────────────────────────┤")
    a=float(eval(input("a=")))
    print("─────────────────────────┤")
    a1=a+1e-10
    if a==0:
        print("您正在进行一元一次方程求解。")
    if a!=0:
        print("您正在进行一元二次方程求解。")
    print("─────────────────────────┤")
    b=float(eval(input("b=")))
    print("─────────────────────────┤")
    c=float(eval(input("c=")))
    print("─────────────────────────┤")
    if a!=0:
        disc=b**2-4*a*c#判别式Δ=b²-4ac
        q=disc**0.5/(2*a)
        p=(-b)/(2*a)
        x1=p+q
        x2=p-q
        j=disc
    d2=b**2-4*a1*c
    q2=d2**0.5/(2*a1)
    p1=(-b)/(2*a1)
    x3=p1+q2
    if a!=0 and j>0:
        print("有两个不相等的实根。\nx1={0:.15f}".format(x1),"\nx2={0:.15f}\n".format(x2),"({0:g},\n".format(x1),"{0:g})".format(x2))
    if a!=0 and j<0:
        print("有两个不相等的虚根。\nx1={0:.15f}".format(x1),"\nx2={0:.15f}\n".format(x2),"({0:g},\n".format(x1),"{0:g})".format(x2))
    if a!=0 and j==0:
        print("有两个相等的实根。\nx1=x2={0:.15f}={0:g}".format(x1))
    if a==0 and b!=0:
        print("此一元一次方程有解。\nx={0:.10f}={0:g}".format(x3))
    if b==0 and a==0 and c!=0:
        print("c({0:g})为非零实数.".format(c))
    if a==0 and b==0 and c==0:
        print("c为零。")
    ii=input("Do you want to continue?(y/n)")
    if ii=="y" or ii=="Y":
        print("ok")
    if ii=="n" or ii=="N":
        break
    
