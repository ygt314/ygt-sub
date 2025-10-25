'''
Function
函数相关计算
(by YGT)
'''
from mymath import *
x=0;n=0
inf=10**12;s=1e-12
ll,mm,rr='l','m','r'
def fx(f,n=x):
    global x
    x=n
    return eval(f)

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
    while abs(a-b)>=s:
        c=(a+b)/2;fa=cn_rn(fx(f,a));fc=cn_rn(fx(f,c))
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
    for i in range(0,n):
        x=fx(f,x)
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
def dfx(f,x=0,lmr=mm):
    '''f'(x)=dy/dx'''
    dx=1e-7;x1=x-dx;x2=x+dx
    if lmr==ll:
        dy=fx(f,x)-fx(f,x1)
    if lmr==mm:
        dy=(fx(f,x2)-fx(f,x1))/2
    if lmr==rr:
        dy=fx(f,x2)-fx(f,x)
    return dy/dx
def newt(f,x0=1e-7,n=100):
    '''newton tangent order'''
    x=x0
    for i in range(0,n):
        x=x-fx(f,x)/dfx(f,x)
    return x
def dnfx(f,x=0,n=2,lmr=mm):
    '''f"(x)=d"y/dx"'''
    dx=10**(-7/(2+n));x1=x-dx;x2=x+dx
    if n<2:
        return dfx(f,x,lmr)    
    if lmr==ll:
        dy=dnfx(f,x,n-1,ll)-dnfx(f,x1,n-1,ll)
    if lmr==mm:
        dy=(dnfx(f,x2,n-1)-dnfx(f,x1,n-1))/2
    if lmr==rr:
        dy=dnfx(f,x2,n-1,rr)-dnfx(f,x,n-1,rr)
    return dy/dx

def sumx(f,x0=1,x1=100):
    '''sum of f'''
    ans=0
    for x in range(x0,x1+1):
        ans+=fx(f,x)
    return ans
def afx(f,a=1e-7,b=1+1e-7,n=1000):
    '''evaluate function average in [a,b]'''
    dx=b-a;total=0
    for i in range(n):
        x=a+(i+0.5)*dx/n # 中点矩形法
        total+=fx(f,x)
    return total/n

def inte(f,a=1e-7,b=1+1e-7,method='simpson',n=9**5):
    '''integrate f in [a,b]
    method is "rect" or "simpson"
    n is best 9**5
    '''
    dx=b-a
    if method=='rect':
        avg=afx(f,a,b,n) #矩形法
        return avg*dx
    elif method=='simpson': #辛普森法
        n+=(n%2) #保持偶数
        h=dx/(n+1)
        total=fx(f,a)+fx(f,b)
        for i in range(1,n+1):
            x=a+i*h
            weight=2+(i%2)*2
            total+=weight*fx(f,x)
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
    '''relative integrate f in [a,b]
    method is "rect" or "simpson"
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
    dx=b-a
    if method=='rect':
        string=f"'{f}',{a},x"
        f=f"ninte({string},{n-1},'rect')"
        avg=afx(f,a,b,points) #矩形法
        return avg*dx
    elif method=='simpson': #辛普森法
        '''递归计算重积分'''
        return inte_sim(f,a,b,n,points)
"""
下述为拓展函数，包含实验性功能
"""
def ninte_vars(f, intervals, method='simpson', depth=0):
    '''
    递归方法计算n重积分
    f: 被积函数字符串，可包含x0,x1,...变量
    intervals: 积分区间列表
    method: 积分方法 ('rect' 或 'simpson')
    depth: 当前递归深度（内部使用）
    '''
    global x
    if len(intervals) == 0:
        return 0
    if len(intervals) == 1:
        # 单重积分，使用现有的inte函数
        a, b = intervals[0]
        return inte(f, a, b, method)
    # 递归处理：将n重积分转化为(n-1)重积分
    current_interval = intervals[0]
    remaining_intervals = intervals[1:]
    def outer_integrand(*outer_vars):
        # 构建内层积分的函数
        inner_f = f
        # 将外层变量固定
        # 这里需要根据实际的变量命名规则调整
        return ninte_vars(inner_f, remaining_intervals, method, depth+1)
    # 对外层变量积分（这里简化处理，实际需要更复杂的变量绑定）
    a, b = current_interval
    return inte(lambda x_val: outer_integrand(x_val), a, b, method)

def ode_solve(f, y0, t_range, method='euler', n=1000):
    '''
    常微分方程数值解
    dy/dt = f(t, y)
    f: 函数字符串，如 't + y'
    y0: 初始值
    t_range: 时间区间 [t0, tf]
    method: 'euler', 'rk4'
    '''
    t0, tf = t_range
    h = (tf - t0) / n
    t = t0; y = y0
    result = [(t, y)]
    
    for i in range(n):
        if method == 'euler':
            y += h * fx(f, t, y)
        elif method == 'rk4':
            k1 = fx(f, t, y)
            k2 = fx(f, t + h/2, y + h*k1/2)
            k3 = fx(f, t + h/2, y + h*k2/2)
            k4 = fx(f, t + h, y + h*k3)
            y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
        result.append((t, y))
    return result

def partial_derivative(f, point, var_index=0, h=1e-7):
    '''
    计算多元函数的偏导数
    f: 多元函数，如 'x**2 + y**2'
    point: 点的坐标 [x0, y0, ...]
    var_index: 对哪个变量求偏导
    '''
    point_plus = point.copy()
    point_minus = point.copy()
    point_plus[var_index] += h
    point_minus[var_index] -= h
    
    # 扩展fx函数支持多变量
    def eval_at_point(p):
        return eval(f, {f'x{i}': p[i] for i in range(len(p))})
    
    derivative = (eval_at_point(point_plus) - eval_at_point(point_minus)) / (2*h)
    return derivative

def normal_pdf(x, mu=0, sigma=1):
    '''正态分布概率密度函数'''
    return 1/(sigma*ma.sqrt(2*pi)) * ma.exp(-0.5*((x-mu)/sigma)**2)

def monte_carlo_integrate(f, bounds, n=10000):
    '''
    蒙特卡洛积分
    bounds: [(a1,b1), (a2,b2), ...] 每个变量的积分区间
    '''
    import random
    total = 0
    dim = len(bounds)
    volume = 1
    for a, b in bounds:
        volume *= (b - a)
    
    for i in range(n):
        point = [random.uniform(a, b) for a, b in bounds]
        total += eval(f, {f'x{j}': point[j] for j in range(dim)})
    return total * volume / n
