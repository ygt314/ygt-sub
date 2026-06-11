# tri_solve_enhanced.py
"""
增强版三角形求解器
保留原有逻辑，结合mpmath提高精度
"""

from mymath_real import *
from myfunc import *

# 显式导入所有原有函数
from tri_solve import (
    tgt as orig_tgt, modA as orig_modA, sABC as orig_sABC, conA as orig_conA,
    _positive as orig_positive, A_j as orig_A_j, AB_j as orig_AB_j, 
    ABC_j as orig_ABC_j, abc_j as orig_abc_j, sa as orig_sa, ca as orig_ca,
    asa as orig_asa, aca as orig_aca, sa_ca as orig_sa_ca, ca_sa as orig_ca_sa,
    AB_C as orig_AB_C, abc_C as orig_abc_C, abC_c as orig_abC_c,
    abA_B as orig_abA_B, ABa_b as orig_ABa_b, ab_c as orig_ab_c,
    abc_ABC as orig_abc_ABC, abC_ABc as orig_abC_ABc, abA_BCc as orig_abA_BCc,
    ABc_Cab as orig_ABc_Cab, ABa_Cbc as orig_ABa_Cbc, ABC_abc as orig_ABC_abc,
    cabc as orig_cabc, sabc as orig_sabc, qinjz as orig_qinjz, 
    helen as orig_helen, sabsC as orig_sabsC, ma as orig_ma, ha as orig_ha,
    la as orig_la, mabc as orig_mabc, habc as orig_habc, labc as orig_labc,
    Rabc as orig_Rabc, rabc as orig_rabc
)

# 条件导入mpmath，如果不可用则回退到原有计算
try:
    import mpmath as mp
    MP_AVAILABLE = True
    # 设置默认精度
    mp.mp.dps = 30
except ImportError:
    MP_AVAILABLE = False
    print("警告: mpmath不可用，使用标准精度计算")

# 配置开关 - 用户可以选择使用高精度模式
USE_HIGH_PRECISION = True and MP_AVAILABLE

# 保留原有配置
sct="a";abc="A"
deg="d";rad="r"

# 精度控制参数
DEFAULT_PRECISION = 30
TOLERANCE = mp.mpf(f'1e-{DEFAULT_PRECISION//2}') if USE_HIGH_PRECISION else 1e-12

def _to_mp(value):
    """将值转换为mpmath格式（如果启用高精度）"""
    if USE_HIGH_PRECISION and MP_AVAILABLE:
        if isinstance(value, (int, float)):
            return mp.mpf(value)
        elif isinstance(value, complex):
            return mp.mpc(value)
        elif hasattr(value, '__iter__'):
            return [_to_mp(v) for v in value]
    return value

def _from_mp(value, precision=DEFAULT_PRECISION, as_string=False):
    """从mpmath格式转换回普通数值
    as_string: 如果为True，返回高精度字符串表示；否则返回Python浮点数/复数
    """
    if USE_HIGH_PRECISION and MP_AVAILABLE:
        if hasattr(value, '__str__'):
            # mpmath类型
            if hasattr(value, 'imag') and value.imag != 0:
                if as_string:
                    real_str = mp.nstr(value.real, precision)
                    imag_str = mp.nstr(value.imag, precision)
                    # 确保虚部有符号
                    if not imag_str.startswith('-'):
                        imag_str = '+' + imag_str
                    return f"{real_str}{imag_str}j"
                else:
                    return complex(mp.nstr(value.real, precision), mp.nstr(value.imag, precision))
            else:
                if as_string:
                    return mp.nstr(value, precision)
                else:
                    return float(mp.nstr(value, precision))
        elif hasattr(value, '__iter__'):
            return [_from_mp(v, precision, as_string) for v in value]
    # 高精度未启用时的处理
    if as_string:
        if hasattr(value, '__iter__'):
            return [str(v) for v in value]
        else:
            # 根据精度格式化字符串
            if isinstance(value, complex):
                return f"{value.real:.{precision}g}+{value.imag:.{precision}g}j"
            else:
                return format(value, f'.{precision}g')
    return value

def _mp_sin(x, dd='r'):
    """高精度正弦函数"""
    if not USE_HIGH_PRECISION:
        return orig_sa(x, dd)
    
    x_mp = _to_mp(x)
    if dd == 'd':
        x_mp = mp.radians(x_mp)
    return mp.sin(x_mp)

def _mp_cos(x, dd='r'):
    """高精度余弦函数"""
    if not USE_HIGH_PRECISION:
        return orig_ca(x, dd)
    
    x_mp = _to_mp(x)
    if dd == 'd':
        x_mp = mp.radians(x_mp)
    return mp.cos(x_mp)

def _mp_acos(x, dd='r'):
    """高精度反余弦函数"""
    if not USE_HIGH_PRECISION:
        return orig_aca(x, dd)
    
    x_mp = _to_mp(x)
    # 数值边界处理
    if x_mp > 1:
        x_mp = mp.mpf(1)
    elif x_mp < -1:
        x_mp = mp.mpf(-1)
    
    result = mp.acos(x_mp)
    if dd == 'd':
        result = mp.degrees(result)
    return result

def _mp_asin(x, dd='r'):
    """高精度反正弦函数"""
    if not USE_HIGH_PRECISION:
        return orig_asa(x, dd)
    
    x_mp = _to_mp(x)
    # 数值边界处理
    if x_mp > 1:
        x_mp = mp.mpf(1)
    elif x_mp < -1:
        x_mp = mp.mpf(-1)
    
    result = mp.asin(x_mp)
    if dd == 'd':
        result = mp.degrees(result)
    return result

def _mp_sqrt(x):
    """高精度平方根"""
    if not USE_HIGH_PRECISION:
        return x**0.5
    return mp.sqrt(_to_mp(x))

# ========== 重新定义关键函数，内部使用高精度计算 ==========

def tgt(dd=rad):
    '''直角90°(pi/2) - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_tgt(dd)
    
    if dd == deg:
        return mp.mpf(90)
    else:
        return mp.pi / 2

def modA(A, dd=rad):
    '''余角=直角-A - 增强版'''
    return tgt(dd) - A

def sABC(dd=rad):
    '''三角形内角和(平角) - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_sABC(dd)
    
    if dd == deg:
        return mp.mpf(180)
    else:
        return mp.pi

def conA(A, dd=rad):
    '''补角=平角-A - 增强版'''
    return sABC(dd) - A

def _positive(a):
    '''边角正数性 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_positive(a)
    
    tolerance = TOLERANCE
    a_val = _to_mp(a)
    return a_val > -tolerance and abs(a_val) > tolerance

def A_j(A, dd=rad):
    '''A∈(0,π) - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_A_j(A, dd)
    return _positive(A) and _positive(conA(A, dd))

def AB_j(A, B, dd=rad):
    '''两角和小于平角 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_AB_j(A, B, dd)
    return _positive(conA(A + B, dd))

def ABC_j(A, B, C, dd=rad):
    '''三角形内角和判断 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_ABC_j(A, B, C, dd)
    
    dis = A + B + C - sABC(dd)
    ans = abs(dis) < TOLERANCE
    _s = [A, B, C, A, B, C]
    for i in range(3):
        if not AB_j(_s[i], _s[i+1], dd):
            ans = False
    return ans

def abc_j(a, b, c):
    '''两边之和大于第三边 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_abc_j(a, b, c)
    
    _s = [a, b, c, a, b, c]
    abcj = True
    for i in range(3):
        dis = _s[i] + _s[i+1] - _s[i+2]
        if abs(dis) < TOLERANCE:
            abcj = False
        if _s[i] + _s[i+1] < _s[i+2]:
            abcj = False
    return abcj

def sa(ns, dd=rad):
    '''A->sinA - 增强版'''
    return _mp_sin(ns, dd)

def ca(ns, dd=rad):
    '''A->cosA - 增强版'''
    return _mp_cos(ns, dd)

def asa(ns, dd=rad, xx="+"):
    '''sinA->A - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_asa(ns, dd, xx)
    
    ns_mp = _to_mp(ns)
    # 数值边界处理
    if ns_mp > 1: ns_mp = mp.mpf(1)
    if ns_mp < -1: ns_mp = mp.mpf(-1)
    
    A = _mp_asin(ns_mp, 'r')  # 始终先计算弧度
    if dd == 'd':
        A = mp.degrees(A)
    
    A2 = conA(A, dd)
    return A if xx == "+" else A2

def aca(ns, dd=rad):
    '''cosA->A - 增强版'''
    return _mp_acos(ns, dd)

def sa_ca(sa_val, xx="+"):
    '''sinA->cosA - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_sa_ca(sa_val, xx)
    
    sa_mp = _to_mp(sa_val)
    ca_val = _mp_sqrt(1 - sa_mp * sa_mp)
    ca_val = ca_val if xx == "+" else -ca_val
    return _from_mp(ca_val)

def ca_sa(ca_val):
    '''cosA->sinA - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_ca_sa(ca_val)
    
    ca_mp = _to_mp(ca_val)
    sa_val = _mp_sqrt(1 - ca_mp * ca_mp)
    return _from_mp(sa_val)

# ========== 关键计算函数的增强版本 ==========

def AB_C(A, B, abc="A", dd=rad):
    '''三角形内角和定理A,B->C - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_AB_C(A, B, abc, dd)
    
    C = conA(A + B, dd)
    sinC = sa(A + B, dd)
    cosC = -ca(A + B, dd)
    scC = [_from_mp(sinC), _from_mp(cosC)]
    varC = _from_mp(C) if abc == "A" else scC
    var0 = 0 if abc == "A" else []
    return varC if AB_j(A, B, dd) else var0

def abc_C(a, b, c, abc="A", dd=rad):
    '''余弦定理:a,b,c->C - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_abc_C(a, b, c, abc, dd)
    
    # 转换为适当精度
    a_val, b_val, c_val = _to_mp(a), _to_mp(b), _to_mp(c)
    
    # 核心计算逻辑保持不变
    cosC = (a_val*a_val + b_val*b_val - c_val*c_val) / (2 * a_val * b_val)
    
    # 数值稳定性处理
    if cosC > 1: cosC = _to_mp(1)
    if cosC < -1: cosC = _to_mp(-1)
    
    C = aca(cosC, dd)
    sinC = ca_sa(cosC)
    
    scC = [_from_mp(sinC), _from_mp(cosC)]
    varC = _from_mp(C) if abc == "A" else scC
    
    return varC

def abC_c(a, b, C, abc="A", dd=rad):
    '''余弦定理:a,b,C->c - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_abC_c(a, b, C, abc, dd)
    
    a_val, b_val = _to_mp(a), _to_mp(b)
    cosC_val = ca(C, dd)
    
    # 核心逻辑保持不变
    c2 = a_val*a_val + b_val*b_val - 2*a_val*b_val*cosC_val
    c_val = _mp_sqrt(c2)
    
    varc = c_val if abc == "A" else c2
    return _from_mp(varc)

def abA_B(a, b, A, abc="A", dd=rad, xx="+"):
    '''正弦定理:a,b,A->B - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_abA_B(a, b, A, abc, dd, xx)
    
    sinB = b * sa(A, dd) / a
    B = asa(sinB, dd, xx)
    cosB = sa_ca(sinB, xx)
    scB = [_from_mp(sinB), _from_mp(cosB)]
    varB = _from_mp(B) if abc == "A" else scB
    return varB

def ABa_b(A, B, a, abc="A", dd=rad):
    '''正弦定理:A,B,a->b - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_ABa_b(A, B, a, abc, dd)
    
    if not A_j(A,dd):
        return 0
    b = a * sa(B, dd) / sa(A, dd)
    b2 = b * b
    varb = b if abc == "A" else b2
    return _from_mp(varb)

def ab_c(ab, AB, abc="A", dd=rad):
    '''射影定理:[a,b],[A,B]->c - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_ab_c(ab, AB, abc, dd)
    
    a, b = ab
    A, B = AB
    c = a * ca(B, dd) + b * ca(A, dd)
    c2 = c * c
    varc = c if abc == "A" else c2
    return varc

# ========== 三角形分类求解函数 - 增强版 ==========

def abc_ABC(a, b, c, abc="A", dd=rad):
    '''SSS(三边对三角) - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_abc_ABC(a, b, c, abc, dd)
    
    A = abc_C(b, c, a, abc, dd)
    B = abc_C(c, a, b, abc, dd)
    C = abc_C(a, b, c, abc, dd)
    return [[A, B, C], [a, b, c]] if abc_j(a, b, c) else []

def abC_ABc(a, b, C, abc="A", dd=rad):
    '''SAS(两边夹一角) - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_abC_ABc(a, b, C, abc, dd)
    
    c0 = abC_c(a, b, C, 'A', dd)
    c = abC_c(a, b, C, abc, dd)
    A = abc_C(b, c0, a, abc, dd)
    B = abc_C(c0, a, b, abc, dd)
    ans = abc_j(a, b, c) and A_j(A, dd)
    return [[A, B, C], [a, b, c]] if ans else []

def abA_BCc(a, b, A, abc="A", dd=rad, xx="+"):
    '''SSA(两边对一角) - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_abA_BCc(a, b, A, abc, dd, xx)
    
    B0 = abA_B(a, b, A, 'A', dd, xx)
    B = abA_B(a, b, A, abc, dd, xx)
    C = AB_C(A, B0, abc, dd)
    c = ab_c([a, b], [A, B0], abc, dd)
    ans = abc_j(a, b, c) and A_j(A, dd)
    return [[A, B, C], [a, b, c]] if ans else []

def ABc_Cab(A, B, c, abc="A", dd=rad):
    '''ASA(两角夹一边) - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_ABc_Cab(A, B, c, abc, dd)
    
    C0 = AB_C(A, B, 'A', dd)
    C = AB_C(A, B, abc, dd)
    a = ABa_b(C0, B, c, abc, dd)
    b = ABa_b(C0, A, a, abc, dd)
    ans = abc_j(a, b, c) and ABC_j(A, B, C0, dd)
    return [[A, B, C], [a, b, c]] if ans else []

def ABa_Cbc(A, B, a, abc="A", dd=rad):
    '''AAS(两角对一边) - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_ABa_Cbc(A, B, a, abc, dd)
    
    C0 = AB_C(A, B, 'A', dd)
    C = AB_C(A, B, abc, dd)
    b = ABa_b(A, B, a, abc, dd)
    c = ABa_b(A, C0, a, abc, dd)
    ans = abc_j(a, b, c) and ABC_j(A, B, C0, dd)
    return [[A, B, C], [a, b, c]] if ans else []

def ABC_abc(A, B, C=0, abc="A", dd=rad):
    '''AAA(三角对三边) - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_ABC_abc(A, B, C, abc, dd)
    
    C0 = AB_C(A, B, 'A', dd) if C == 0 else C
    C1 = AB_C(A, B, abc, dd)
    b = ABa_b(A, B, 1, abc, dd)
    c = ABa_b(A, C0, 1, abc, dd)
    return [[A, B, C1], [1, b, c]] if ABC_j(A, B, C0, dd) else []

# ========== 面积和相关计算 - 增强版 ==========

def cabc(a, b, c):
    '''周长 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_cabc(a, b, c)
    return a + b + c

def sabc(a, b, c):
    '''半周长 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_sabc(a, b, c)
    return cabc(a, b, c) / 2

def qinjz(a, b, c):
    '''秦九昭公式 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_qinjz(a, b, c)
    
    a_val, b_val, c_val = _to_mp(a), _to_mp(b), _to_mp(c)
    
    # 保持原有计算逻辑
    a2, b2, c2 = a_val*a_val, b_val*b_val, c_val*c_val
    ah2 = a2*b2 - ((a2 + b2 - c2)**2) / 4
    area = _mp_sqrt(ah2) / 2
    
    return _from_mp(area)

def helen(a, b, c):
    '''海伦公式 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_helen(a, b, c)
    
    a_val, b_val, c_val = _to_mp(a), _to_mp(b), _to_mp(c)
    
    # 保持原有计算逻辑
    s_val = (a_val + b_val + c_val) / 2
    area = _mp_sqrt(s_val * (s_val - a_val) * (s_val - b_val) * (s_val - c_val))
    
    return _from_mp(area)

def sabsC(a, b, C, dd=rad):
    '''边角面积公式 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_sabsC(a, b, C, dd)
    return _from_mp(a * b * sa(C, dd) / 2)

# ========== 其他几何计算 - 增强版 ==========

def ma(a, b, c):
    '''中线长公式 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_ma(a, b, c)
    
    a_val, b_val, c_val = _to_mp(a), _to_mp(b), _to_mp(c)
    m2 = 2*b_val*b_val + 2*c_val*c_val - a_val*a_val
    return _from_mp(_mp_sqrt(m2) / 2)

def ha(a, b, c, abc="A"):
    '''高线长 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_ha(a, b, c, abc)
    
    a_val, b_val, c_val = _to_mp(a), _to_mp(b), _to_mp(c)
    a2, b2, c2 = a_val*a_val, b_val*b_val, c_val*c_val
    ha2 = b2 - (a2 + b2 - c2)**2 / (a2 * 4)
    ha_val = _mp_sqrt(ha2)
    varh = ha_val if abc == "A" else ha2
    return _from_mp(varh)

def la(a, b, c):
    '''角平分线长 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_la(a, b, c)
    
    a_val, b_val, c_val = _to_mp(a), _to_mp(b), _to_mp(c)
    lab2 = b_val * c_val * ((b_val + c_val)**2 - a_val*a_val)
    return _from_mp(_mp_sqrt(lab2) / (b_val + c_val))

def mabc(a, b, c):
    '''中线长[ma,mb,mc] - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_mabc(a, b, c)
    
    _s = [a, b, c, a, b, c]
    return [ma(_s[i], _s[i+1], _s[i+2]) for i in range(3)]

def habc(a, b, c):
    '''高线长[ha,hb,hc] - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_habc(a, b, c)
    
    _s = [a, b, c, a, b, c]
    return [ha(_s[i], _s[i+1], _s[i+2]) for i in range(3)]

def labc(a, b, c):
    '''角平分线长[la,lb,lc] - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_labc(a, b, c)
    
    _s = [a, b, c, a, b, c]
    return [la(_s[i], _s[i+1], _s[i+2]) for i in range(3)]

def Rabc(a, b, c):
    '''外接圆半径 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_Rabc(a, b, c)
    
    a_val, b_val, c_val = _to_mp(a), _to_mp(b), _to_mp(c)
    s4 = qinjz(a, b, c) * 4
    return _from_mp(a_val * b_val * c_val / s4)

def rabc(a, b, c):
    '''内切圆半径 - 增强版'''
    if not USE_HIGH_PRECISION:
        return orig_rabc(a, b, c)
    
    a_val, b_val, c_val = _to_mp(a), _to_mp(b), _to_mp(c)
    s_val = sabc(a_val, b_val, c_val)
    tabc = (s_val - a_val) * (s_val - b_val) * (s_val - c_val)
    return _from_mp(_mp_sqrt(tabc / s_val))

# ========== 新增精度控制功能 ==========

def set_precision(precision):
    """动态设置计算精度"""
    global USE_HIGH_PRECISION, TOLERANCE, DEFAULT_PRECISION
    
    DEFAULT_PRECISION = precision
    
    if MP_AVAILABLE and precision > 15:  # 只有需要高精度时才启用
        USE_HIGH_PRECISION = True
        mp.mp.dps = precision
        TOLERANCE = mp.mpf(f'1e-{precision//2}')
        print(f"已启用高精度模式: {precision} 位小数")
    else:
        USE_HIGH_PRECISION = False
        # 标准精度下，容差基于精度设置，但不超过双精度极限
        effective_precision = min(12, precision) if precision > 0 else 12
        TOLERANCE = 10 ** (-effective_precision)
        print(f"使用标准精度模式: 容差 {TOLERANCE}")

def get_calculation_mode():
    """获取当前计算模式"""
    return "高精度" if USE_HIGH_PRECISION else "标准精度"

# ========== 测试代码 ==========

if __name__ == "__main__":
    print("=== 三角形求解器测试 ===")
    print(f"模式: {get_calculation_mode()}, MPmath: {MP_AVAILABLE}")
    
    # 1. 基本三角形计算
    a, b, c = 3, 4, 5
    print(f"\n1. 基本测试 (a={a}, b={b}, c={c}):")
    
    rads = abc_ABC(a, b, c)
    if rads:
        A, B, C = rads[0]
        print(f"   角度: {A:.6f}, {B:.6f}, {C:.6f}")
        
        area1 = qinjz(a, b, c)
        area2 = helen(a, b, c)
        print(f"   面积: 秦九昭={area1}, 海伦={area2}, 差异={abs(area1 - area2):.2e}")
    else:
        print("   无效三角形")
    
    # 2. 精度控制演示
    if MP_AVAILABLE:
        print("\n2. 精度控制演示:")
        
        # 展示不同精度下的 sin(π/3)
        precisions = [15, 30, 50]
        for prec in precisions:
            set_precision(prec)
            sin_val = sa(mp.pi/3) if USE_HIGH_PRECISION else sa(3.141592653589793/3)
            sin_str = _from_mp(sin_val, as_string=True)
            print(f"   精度{prec:2d}位: sin(π/3) = {sin_str}")
        
        # 恢复默认精度
        set_precision(DEFAULT_PRECISION)
        
        # 3. 关键特性验证
        print("\n3. 关键特性验证:")
        
        # 容差统一性
        print(f"   当前容差: {TOLERANCE}")
        test_val = mp.mpf('1e-20')
        near_pi_angle = mp.pi + test_val
        is_valid = ABC_j(float(near_pi_angle), 0, 0)
        print(f"   π+{test_val} 是否有效角: {is_valid}")
        
        # 高精度输出
        sqrt2_str = _from_mp(mp.sqrt(2), as_string=True)
        print(f"   √2 高精度: {sqrt2_str[:20]}...")
        
        # 退化三角形判断
        a_test, b_test, c_test = 1, 1, 2 - 1e-15
        is_triangle = abc_j(a_test, b_test, c_test)
        print(f"   退化判断 (1,1,{c_test:.15f}): {is_triangle}")
    
    print("\n=== 测试完成 ===")