'''
Function
函数相关计算
(by YGT)
'''
from mymath import *
x=0;n=0
inf=10**12;s=1e-12
ll,mm,rr='l','m','r'
eq,eq1,func='equa','equa1','func'
#get f(x)
_ff=lambda f:f if able_(f) else "x"
_fx=lambda f:eval("lambda x:"+_ff(f))
get_fx=_fx
def fx(f,xx=0):
    '''单次计算f(x)，并改变全局x'''
    global x
    x,ff=xx,_fx(f)
    return ff(x)
def bisec(f,a=-100,b=100,s=1e-12):
    '''
二分法求函数零点
f:[function string]
e.g.'x+1' is f(x)=x+1
[a,b]:available interval
指定区间[a,b]
s:precision
s为精度
'''
    ff=_fx(f)
    while abs(a-b)>=s:
        c=(a+b)/2;fa=cn_rn(ff(a));fc=cn_rn(ff(c))
        if type(fa)==complex or type(fc)==complex:
            a=c;continue
        if fa*fc<0:
            b=c
        elif fc==0:
            a=c;break
        else:
            a=c
    return a
def xfx(f,x=0,n=100):
    '''不动点求解'''
    ff=_fx(f)
    for i in range(0,n):
        x=ff(x)
    return x

def lim(f,n=0,lmr=mm):
    '''
lim:limit for f
f:function f(x)
n:limif to num
lmr:ll is left,mm is mid,rr is right
'''
    s=1e-12;x1=n-s;x2=n+s
    if lmr==ll:
        ans=fx(f,x1)
    if lmr==mm:
        ans=(fx(f,x1)+fx(f,x2))/2
    if lmr==rr:
        ans=fx(f,x2)
    return ans
def dff(ff,x=1e-7,lmr=mm):
    '''f'(x)=dy/dx'''
    n=7;dx=10**(-n);x1=x-dx;x2=x+dx
    if lmr==ll:
        dy=ff(x)-ff(x1)
    if lmr==mm:
        dy=(ff(x2)-ff(x1))/2
    if lmr==rr:
        dy=ff(x2)-ff(x)
    return dy*10**n
def dfx(f,xx=1e-7,lmr=mm):
    global x
    x,ff=xx,_fx(f)
    return dff(ff,x,lmr)
def newt(f,x0=1e-7,n=100):
    '''newton tangent order'''
    x,ff=x0,_fx(f)
    for i in range(0,n):
        x=x-ff(x)/dff(ff,x)
    return x
def dnfx(f,x=1e-7,n=2,lmr=mm):
    '''f"(x)=d"y/dx"'''
    dx=10**(-7/(2+n));x1=x-dx;x2=x+dx
    if n<2:
        return dfx(f,x,lmr)
    # 次数大:误差大，效率低
    if n>15:
        return 0
    if lmr==ll:
        dy=dnfx(f,x,n-1,ll)-dnfx(f,x1,n-1,ll)
    if lmr==mm:
        dy=(dnfx(f,x2,n-1)-dnfx(f,x1,n-1))/2
    if lmr==rr:
        dy=dnfx(f,x2,n-1,rr)-dnfx(f,x,n-1,rr)
    return dy/dx
#function and curve(line)
def format_line(k,b,kb=1):
    '''kb:(0)kx+b or (1)b+kx'''
    b_str=str(b)
    kx_str=f"({k})x" if type==complex else f"{k}x"
    kx_str="x" if k==1 else kx_str
    kx_str="-x" if k==-1 else kx_str
    if kb==1:
        kb_str=b_str+sign_num(kx_str)
    else:
        kb_str=kx_str+sign_num(b_str)
    kb_str=kx_str if abs(b)<1e-7 else kb_str
    kb_str=str(b) if abs(k)<1e-7 else kb_str
    kb_str="0" if abs(b)<1e-7 and abs(k)<1e-7 else kb_str
    return kb_str
def tan_fx(f,x0=1e-7,result='func'):
    '''
    切线方程(一阶泰勒公式)
    x0:切点
    result:'func'返回切线(x部分)表达式,
    'equa'返回切线斜截式方程
    '''
    ff=_fx(f)
    k=cn_rn(dff(ff,x0),14)
    b=cn_rn(ff(x0)-k*x0,8)
    k=cn_rn(dff(ff,x0),8)
    res_j=0 if "1" in result else 1
    kb_str=format_line(k,b,res_j)
    eq_str=f"y={kb_str}"
    return eq_str if result[:4]=='equa' else kb_str
def taylor(f, x0=1e-7, nn=5):
    '''
    计算函数f(x)在x0点的泰勒展开式
    f: 函数字符串，如 'sin(x)'
    x0: 展开点
    nn: 展开阶数（返回n+1项：0阶到n阶）
    返回：泰勒展开式的字符串表示
    '''
    if nn<2: return tan_fx(f,x0)
    from math import factorial
    ff=_fx(f);f0,n=cn_rn(ff(x0)),12 if nn>14 else nn
    # 初始化系数(计算f(x0))
    derivatives,coeff=[f0],f0
    for k in range(1,n+1):
        # 高阶导数
        val = cn_rn(dnfx(f, x0, n=k))
        derivatives.append(val)
    # 构建展开式字符串
    terms = [format_coeff(coeff, is_first=True)]
    for k in range(1,n+1):
        coeff = derivatives[k] / factorial(k)
        coeff = cn_rn(coeff,8-k) if k<7 else cn_rn(coeff,1)
        # 跳过系数为0的项（考虑浮点误差）
        if coeff == 0:
            continue
        # 处理符号
        sign = "+" if coeff.real > 0 else "-"
        sign = "+" if type(coeff)==complex else sign
        abs_coeff = abs(coeff)
        # 处理系数
        if abs_coeff == 1:
            coeff_str = ""
        elif abs_coeff == -1:
            coeff_str = "-"
        else:
            coeff_str = format_coeff(abs_coeff,7)
        # 处理(x-x0)部分
        if k == 1:
            x_part = f"(x{sign_x(x0)})"
        else:
            x_part = f"(x{sign_x(x0)})^{k}"
        term = f"{sign} {coeff_str}{x_part}"
        terms.append(term)
    # 组合所有项
    if not terms:
        return "0"
    result = terms[0]
    for term in terms[1:]:
        result += " " + term
    return result.strip()
def sign_x(x0):
    '''辅助函数：生成x-x0的符号部分'''
    x_str=str(-cn_rn(x0,7))
    if abs(x0) < 1e-7:
        return ""
    elif x_str[0]=="-":
        return x_str
    else:
        return "+"+x_str
def taylor_known(f, n=5):
    '''
    返回常见函数的已知泰勒展开式（麦克劳林级数）
    f: 'sin', 'cos', 'exp', 'ln(1+x)', '1/(1-x)'
    n: 展开阶数
    '''
    known_expansions = {
        'sin': lambda n: " + ".join([f"{'' if i%4==1 else '-' if i%4==3 else ''}x^{i}/{i}" for i in range(1, n+1, 2)]),
        'cos': lambda n: " + ".join([f"{'' if i%4==0 else '-' if i%4==2 else ''}x^{i}/{i}" for i in range(0, n+1, 2)]),
        'exp': lambda n: " + ".join([f"x^{i}/{i}" for i in range(n+1)]),
        'ln(1+x)': lambda n: " + ".join([f"{'' if i%2==1 else '-'}x^{i}/{i}" for i in range(1, n+1)]),
        '1/(1-x)': lambda n: " + ".join([f"x^{i}" for i in range(n+1)]),
    }
    if f in known_expansions:
        return known_expansions[f](n)
    else:
        return f"未知函数：{f}"

if __name__ == "__main__":
    # 测试泰勒展开
    print("sin(x) 在 x=0 处的5阶展开：")
    print(taylor('sin(x)', 0, 5))
    
    print("\ncos(x) 在 x=0 处的4阶展开：")
    print(taylor('cos(x)', 0, 4))
    
    print("\ne^x 在 x=1 处的3阶展开：")
    print(taylor('exp(x)', 1, 3))
    
    print("\nln(x) 在 x=1 处的4阶展开：")
    print(taylor('log(x)', 1, 4))
    
    print("\n已知函数展开式：")
    print("sin(x) =", taylor_known('sin', 5))

def sumx(f,x0=1,x1=100):
    '''sum of f'''
    ans,ff=0,_fx(f)
    for x in range(x0,x1+1):
        ans+=ff(x)
    return ans
def afx(f,a=1e-7,b=1+1e-7,n=1000):
    '''evaluate function average in [a,b]'''
    dx=b-a;total,ff=0,_fx(f)
    for i in range(n):
        x=a+(i+0.5)*dx/n # 中点矩形法
        total+=ff(x)
    return total/n

def inte(f,a=1e-7,b=1+1e-7,method='simpson',n=9**5):
    '''integrate f in [a,b]
    method is "rect" or "simpson"
    n is best 9**5
    '''
    dx,ff=b-a,_fx(f)
    if method=='rect':
        avg=afx(f,a,b,n) #矩形法
        return avg*dx
    elif method=='simpson': #辛普森法
        n+=(n%2) #保持偶数
        h=dx/(n+1)
        total=ff(a)+ff(b)
        for i in range(1,n+1):
            x=a+i*h
            weight=2+(i%2)*2
            total+=weight*ff(x)
        return total*h/3
def _optimized_ninte_points(n, method='simpson'):
    """采样量优化公式"""
    # 方法效率系数=1.0
    # method_efficiency={'rect': 1.0,'simpson': 2.0,'gauss': 3.0}.get(method, 1.5)
    # 基础点数（考虑目标精度1e-3）
    s=1e-3
    base_points = 1/(s*10**(n-2))
    # 维度衰减（非线性衰减，避免高维采样过少）
    if n<2:
        return 100
    else:
        points = base_points*(0.7**(n-1)) # 高维指数衰减
    # points *= method_efficiency
    # 确保最小采样点数和合理性
    min_points=20 if method=='simpson' else 50
    max_points=10**(5/n) # 防止计算资源耗尽
    return max(min_points,min(points,max_points))
def ninte(f,a=1e-7,b=1+1e-7,n=2,method='simpson'):
    '''relative integrate f(x) in [a,b]
    method is "rect" or "simpson"
    单变量n重积分
    '''
    def inte_sim(f,a,b,m,n):
        "辛普森法"
        dx=b-a
        n+=(n%2) #保持偶数
        h=dx/(n+1)
        total=ninte(f,a,b,m-1)
        for i in range(1,n+1):
            x=a+i*h
            weight=2+(i%2)*2
            total+=weight*ninte(f,a,x,m-1)
        return total*h/3
    points=int(_optimized_ninte_points(n,method))
    if n<2:
        return inte(f,a,b,method,points)
    # 次数大:误差大，效率低
    if n>15:
        return 0
    dx=b-a
    if method=='rect':
        string=f"'{f}',{a},x"
        f=f"ninte({string},{n-1},'rect')"
        avg=afx(f,a,b,points) #矩形法
        return avg*dx
    elif method=='simpson': #辛普森法
        '''递归计算重积分'''
        return inte_sim(f,a,b,n,points)
