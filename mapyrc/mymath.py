'''
calculate for math
数学常用计算
(by YGT)
'''
# 在任何其他导入之前设置抑制pypynum输出
import sys
# 检查是否已经设置过，避免重复设置
if 'math_adapter' in sys.modules:
    # 如果 math_adapter 已经被导入，不强制设置抑制，保留现有设置
    pass
else:
    # 如果 math_adapter 还未被导入，先设置全局抑制变量
    from math_adapter import set_global_suppress_pypynum_output
    # 只有在没有明确设置过抑制状态时才使用默认抑制
    import os
    # 检查环境变量是否指定了抑制状态
    if 'SUPPRESS_PYPYNUM_OUTPUT' not in os.environ:
        # 默认抑制pypynum输出
        set_global_suppress_pypynum_output(suppress=True)

# 使用适配层替换原有的math和cmath导入
from math_adapter import (
    sin as _sin, cos as _cos, tan as _tan, 
    asin as _asin, acos as _acos, atan as _atan,
    sinh as _sinh, cosh as _cosh, tanh as _tanh,
    exp as _exp, log as _log, sqrt as _sqrt,
    degrees_to_radians as _d_r, radians_to_degrees as _r_d,
    get_pi as _get_pi, get_e as _get_e,
    abs_value as _abs
)
import cmath as cm  # 保留cmath用于特定复数操作

# 获取数学常量
pi = _get_pi()
e = _get_e()
i = 1j
deg = 'd'
rad = 'r'
s2 = _sqrt(2)
phi = (_sqrt(5) - 1) / 2
gama = 0.57721_56649_01532_8606
s2 = _sqrt(2); phi = (_sqrt(5) - 1) / 2; gama = 0.57721_56649_01532_8606
sss, exps, coeff = 'str', 'expr', 'coeff'

def r_d(r):
    return _r_d(r)

def d_r(d):
    return _d_r(d)

def xsex(n, cale=12):
    '''尝试约化小数部分,但不处理整数
    支持复数,但只处理实部'''
    ans = n
    if type(n) != int:
        f = '.' + str(cale) + 'g'
        # 使用内置format，不使用数学库
        ans = eval(format(n, f))
    ans = ans.imag * 1j if abs(n.real) < 10**(-cale) else ans
    return ans

def cn_rn(c, cale=12):
    '''尝试得到实数'''
    cc = xsex(c, cale)
    ans = cc.real if abs(c.imag) < 10**(-cale) else cc
    return ans

# 分数形式
def format_coeff(coeff, is_first=False):
    '''格式化系数'''
    k = cn_rn(coeff, 7)
    ks = f"({k})" if type(k) == complex else str(k)
    if is_first:
        return ks
    abs_, k_s = _abs(k), ks[1:] if ks[0] == '-' else ks
    if abs(abs_ - 1) < 1e-7:
        k_s = ""
    return k_s

def sign_num(n, mode='str', is_first=False):
    '''显示加号用于拼接表达式
    mode:
    "str":常数项模式(或项与项拼接)
    "expr":表达式模式
    "coeff":系数模式
    is_first:首项专属'''
    n_str = str(n)
    if mode == "expr":
        return f"({n_str})" if is_first else f"+({n_str})"
    if mode == "coeff":
        format_coeff(n, is_first)
    else:
        nss = n_str if n_str[0] == "-" else "+" + n_str
    return n_str if is_first else nss

def xs_fs(num, cale=5):
    '''小数化分数，支持复数'''
    real_str = confs(num.real, cale)
    imag_str = confs(num.imag, cale)
    num_str = real_str + sign_num(imag_str) + "j"
    return num_str

def _getfs(c, cale=12):
    '''获取分数形式，支持2次幂分母
    防止连分数算法不支持精确小数'''
    m = 1 if cale < 1 else cale
    a = c.real
    for i in range(1, 10**6):
        aa = int(a * i)
        if abs(aa - a * i) < 10**(-m):
            return f"{aa}/{i}"
    aa = int(a * 10**m)
    return str(aa) + "/1" + "0" * m

def confs(c, cale=5):
    '''连分数算法'''
    a, j = c.real, 0
    a_j = "-" if a < 0 else ""
    p0, q0, p1, q1, n = 0, 1, 1, 0, 10**(cale)
    if abs(a - int(a)) < 10**(-cale): 
        return str(int(a))
    n, a = 10 if n < 10 else int(n), abs(a)
    while True:
        b = int(a)
        if b == a:
            j = 1
            break
        p2 = b * p1 + p0
        q2 = b * q1 + q0
        if q2 > n:
            break
        p0, q0, p1, q1 = p1, q1, p2, q2
        a = 1 / (a - b)
    return f"{a_j}{p1}/{q1}" if j == 0 else _getfs(c, cale)

# 三角函数
# 正弦
def sin(n, dd='r'):
    r = d_r(n) if dd == deg else n
    # 使用适配层，但保留复数支持
    return _sin(r)

# 余割
def csc(n, dd='r'):
    r = d_r(n) if dd == deg else n
    # 使用适配层
    return 1 / _sin(r)

# 余弦
def cos(n, dd='r'):
    r = d_r(n) if dd == deg else n
    # 使用适配层
    return _cos(r)

# 正割
def sec(n, dd='r'):
    r = d_r(n) if dd == deg else n
    # 使用适配层
    return 1 / _cos(r)

# 正切
def tan(n, dd='r'):
    r = d_r(n) if dd == deg else n
    # 使用适配层
    return _tan(r)

# 余切
def cot(n, dd='r'):
    r = d_r(n) if dd == deg else n
    # 使用适配层
    return 1 / _tan(r)

# 双曲函数 - 使用适配层
sinh = _sinh
cosh = _cosh
tanh = _tanh
asinh = cm.asinh  # Python的cmath模块提供了这些函数
acosh = cm.acosh
atanh = cm.atanh

# 反正弦
def asin(n, dd='r'):
    r = _asin(n)
    d = r_d(r) if dd == deg else r
    return d

# 反余割
def acsc(n, dd='r'):
    r = _asin(1 / n)
    d = r_d(r) if dd == deg else r
    return d

# 反余弦
def acos(n, dd='r'):
    r = _acos(n)
    d = r_d(r) if dd == deg else r
    return d

# 反正割
def asec(n, dd='r'):
    r = _acos(1 / n)
    d = r_d(r) if dd == deg else r
    return d

# 反正切
def atan(n, dd='r'):
    r = _atan(n)
    d = r_d(r) if dd == deg else r
    return d

# 反余切
def acot(n, dd='r'):
    r = _atan(1 / n)
    d = r_d(r) if dd == deg else r
    return d

# 使用适配层的数学函数
sqrt = _sqrt
cbrt = lambda x: x**(1/3)  # 保持原来的实现
exp = _exp
exp_10 = lambda x: 10**x  # 保持原来的实现

lg = lambda x: _log(x, 10)  # 以10为底的对数
ln = lambda x: _log(x)      # 自然对数
log = lambda x, base=None: _log(x, base)  # 对数函数

# 使用适配层的函数
floor = lambda x: int(x) if x >= 0 else int(x) - 1  # 基本实现
ceil = lambda x: int(x) if x == int(x) else int(x) + 1 if x >= 0 else int(x)  # 基本实现
def able_(f=''):
    """验证表达式安全性"""
    import re
    # 更精确的黑名单
    dangerous_patterns = [
        r'__[a-zA-Z0-9_]+__',  # 双下划线魔术方法
        r'\bos\b(?![a-zA-Z])',  # 确保os是独立单词，后面不跟字母
        r'\bsys\b',             # sys 模块
        r'\bsubprocess\b',      # subprocess 模块
        r'\bimport\b',          # import 语句
        r'\bexec\b',            # exec 函数
        r'\beval\b',            # eval 函数
        r'\bglobals\b',         # globals 函数
        r'\blocals\b',          # locals 函数
        r'\b__import__\b',      # __import__ 函数
        r'open\s*\(',           # open 函数
        r'compile\s*\(',        # compile 函数
    ]
    # 安全函数白名单（快速通过检查）
    safe_functions = ['acos', 'cos', 'sin', 'tan', 'log', 'sqrt', 'pi', 'e']
    # 如果整个表达式都是安全函数和数字运算符，直接通过
    tokens = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*', f)
    if all(token in safe_functions or token.isdigit() for token in tokens):
        return True
    for pattern in dangerous_patterns:
        if re.search(pattern, f, re.IGNORECASE):
            return False
    return True

inf = 10**12
s = 1e-12

a, b, c, d = -7, -6, -5, -4
m, n = -3, -2
p, q = -1, 1
x, y, z = 2, 3, 4
u, v, w = 5, 6, 7

from formula_str import *
from myfunc import *

def num(n):
    '''n is num?'''
    ans = False
    if type(n) == int or type(n) == float:
        ans = True
    elif type(n) == complex:
        ans = True
    return ans

# 数列
_aa = lambda f: f if able_(f) else "n"  # 修正：使用 able_ 而不是 _able
_an = lambda f: eval("lambda n:" + _aa(f))

def an(f, n=1, m=0):
    '''a_n=f(n),n∈N*'''
    ff = _an(f)
    if m <= n:
        return ff(n) if n > 0 else 0
    return [ff(i) for i in range(n, m + 1)]

def dn(f, n=1, m=0):
    '''d_n=a_(n+1)-a_n,n∈N*'''
    ff = _an(f)
    if m <= n:
        return ff(n) - ff(n - 1)
    return [ff(i) - ff(i - 1) for i in range(n, m + 1)]

def sn(f, n=100, m=0):
    '''a_n=f(n):S_n,n∈N*'''
    ans, ff = 0, _an(f)
    for i in range(1, n + 1):
        ans += ff(i)
    if m <= n:
        return ans
    sns = [ans]
    for i in range(n + 1, m + 1):
        ans += ff(i)
        sns += [ans]
    return sns

if __name__ == "__main__":
    ems = "e**(pi*i)+1"
    ans = eval(ems)
    print(ems, "=", cn_rn(ans))