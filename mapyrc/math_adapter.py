"""
数学库适配层，统一pypynum、numpy和标准库的接口
"""
import math
import sys
import os
import warnings
import io
from contextlib import redirect_stdout

# 全局变量用于控制pypynum输出抑制
# 通过环境变量或默认值来设置
GLOBAL_SUPPRESS_PYPYNUM_OUTPUT = os.environ.get('SUPPRESS_PYPYNUM_OUTPUT', '1').lower() in ('1', 'true', 'yes', 'on')

def set_global_suppress_pypynum_output(suppress):
    """设置全局pypynum输出抑制状态"""
    global GLOBAL_SUPPRESS_PYPYNUM_OUTPUT
    GLOBAL_SUPPRESS_PYPYNUM_OUTPUT = suppress

class MathBackend:
    """数学计算后端管理器"""
    
    def __init__(self, suppress_pypynum_output=None):
        self.backends = {}
        # 如果没有明确指定，则使用全局设置
        if suppress_pypynum_output is None:
            self.suppress_pypynum_output = GLOBAL_SUPPRESS_PYPYNUM_OUTPUT
        else:
            self.suppress_pypynum_output = suppress_pypynum_output
        self._detect_backends()
    
    def _detect_backends(self):
        """检测可用的数学库"""
        # 检测pypynum
        try:
            if self.suppress_pypynum_output:
                # 临时重定向标准输出以抑制pypynum的版本信息
                with redirect_stdout(io.StringIO()):
                    import pypynum
                    self.backends['pypynum'] = pypynum
            else:
                import pypynum
                self.backends['pypynum'] = pypynum
        except ImportError:
            self.backends['pypynum'] = None
        
        # 检测numpy
        try:
            import numpy as np
            self.backends['numpy'] = np
        except ImportError:
            self.backends['numpy'] = None
        
        # math库始终可用
        self.backends['math'] = math
        self.backends['cmath'] = __import__('cmath')
    
    def get_backend(self, preferred='auto'):
        """获取首选的后端"""
        if preferred == 'pypynum' and self.backends['pypynum']:
            return 'pypynum', self.backends['pypynum']
        elif preferred == 'numpy' and self.backends['numpy']:
            return 'numpy', self.backends['numpy']
        elif self.backends['pypynum']:
            return 'pypynum', self.backends['pypynum']
        elif self.backends['numpy']:
            return 'numpy', self.backends['numpy']
        else:
            return 'math', self.backends['math']
    
    def get_cmath_backend(self, preferred='auto'):
        """获取支持复数的后端"""
        if preferred == 'pypynum' and self.backends['pypynum']:
            return 'pypynum', self.backends['pypynum']
        elif preferred == 'numpy' and self.backends['numpy']:
            return 'numpy', self.backends['numpy']
        else:
            return 'cmath', self.backends['cmath']

# 创建全局后端管理器（默认不抑制pypynum输出）
# 但在模块加载时检查是否需要全局抑制
backend_manager = MathBackend()


def set_pypynum_output(suppress=True):
    """设置是否抑制pypynum的输出信息"""
    set_global_suppress_pypynum_output(suppress)
    global backend_manager
    # 重新创建后端管理器以应用新设置
    backend_manager = MathBackend()


def sin(x, preferred_backend='auto'):
    """正弦函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.sin(x)
    elif backend_type == 'numpy':
        return backend.sin(x)
    else:  # cmath or math
        if isinstance(x, complex) or x != x:  # complex or nan
            return backend.sin(x)
        else:
            return backend.sin(float(x))


def cos(x, preferred_backend='auto'):
    """余弦函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.cos(x)
    elif backend_type == 'numpy':
        return backend.cos(x)
    else:  # cmath or math
        if isinstance(x, complex) or x != x:  # complex or nan
            return backend.cos(x)
        else:
            return backend.cos(float(x))


def tan(x, preferred_backend='auto'):
    """正切函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.tan(x)
    elif backend_type == 'numpy':
        return backend.tan(x)
    else:  # cmath or math
        if isinstance(x, complex) or x != x:  # complex or nan
            return backend.tan(x)
        else:
            return backend.tan(float(x))


def exp(x, preferred_backend='auto'):
    """指数函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.exp(x)
    elif backend_type == 'numpy':
        return backend.exp(x)
    else:  # cmath or math
        if isinstance(x, complex) or x != x:  # complex or nan
            return backend.exp(x)
        else:
            return backend.exp(float(x))


def log(x, base=None, preferred_backend='auto'):
    """对数函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        if base is None:
            return backend.log(x)
        else:
            return backend.log(x) / backend.log(base)
    elif backend_type == 'numpy':
        if base is None:
            return backend.log(x)
        elif base == 10:
            return backend.log10(x)
        elif base == 2:
            return backend.log2(x)
        else:
            return backend.log(x) / backend.log(base)
    else:  # cmath or math
        if isinstance(x, complex) or x != x:  # complex or nan
            if base is None:
                return backend.log(x)
            else:
                return backend.log(x) / backend.log(base)
        else:
            x = float(x)
            if base is None:
                return backend.log(x)
            elif base == 10:
                return backend.log10(x)
            elif base == 2:
                return backend.log2(x)
            else:
                return backend.log(x) / backend.log(base)


def sqrt(x, preferred_backend='auto'):
    """平方根函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.sqrt(x)
    elif backend_type == 'numpy':
        return backend.sqrt(x)
    else:  # cmath or math
        if isinstance(x, complex) or x < 0 or x != x:  # complex, negative or nan
            return backend.sqrt(x)
        else:
            return backend.sqrt(float(x))


def asin(x, preferred_backend='auto'):
    """反正弦函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.asin(x)
    elif backend_type == 'numpy':
        return backend.arcsin(x)
    else:  # cmath or math
        if isinstance(x, complex) or abs(x) > 1 or x != x:  # complex or out of domain or nan
            return backend.asin(x)
        else:
            return backend.asin(float(x))


def acos(x, preferred_backend='auto'):
    """反余弦函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.acos(x)
    elif backend_type == 'numpy':
        return backend.arccos(x)
    else:  # cmath or math
        if isinstance(x, complex) or abs(x) > 1 or x != x:  # complex or out of domain or nan
            return backend.acos(x)
        else:
            return backend.acos(float(x))


def atan(x, preferred_backend='auto'):
    """反正切函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.atan(x)
    elif backend_type == 'numpy':
        return backend.arctan(x)
    else:  # cmath or math
        if isinstance(x, complex) or x != x:  # complex or nan
            return backend.atan(x)
        else:
            return backend.atan(float(x))


def sinh(x, preferred_backend='auto'):
    """双曲正弦函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.sinh(x)
    elif backend_type == 'numpy':
        return backend.sinh(x)
    else:  # cmath or math
        if isinstance(x, complex) or x != x:  # complex or nan
            return backend.sinh(x)
        else:
            return backend.sinh(float(x))


def cosh(x, preferred_backend='auto'):
    """双曲余弦函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.cosh(x)
    elif backend_type == 'numpy':
        return backend.cosh(x)
    else:  # cmath or math
        if isinstance(x, complex) or x != x:  # complex or nan
            return backend.cosh(x)
        else:
            return backend.cosh(float(x))


def tanh(x, preferred_backend='auto'):
    """双曲正切函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.tanh(x)
    elif backend_type == 'numpy':
        return backend.tanh(x)
    else:  # cmath or math
        if isinstance(x, complex) or x != x:  # complex or nan
            return backend.tanh(x)
        else:
            return backend.tanh(float(x))


def degrees_to_radians(x, preferred_backend='auto'):
    """角度转弧度"""
    backend_type, backend = backend_manager.get_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        pi_val = get_pi('pypynum')
        return x * pi_val / 180
    elif backend_type == 'numpy':
        return backend.radians(x)
    else:
        return x * math.pi / 180


def radians_to_degrees(x, preferred_backend='auto'):
    """弧度转角度"""
    backend_type, backend = backend_manager.get_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        pi_val = get_pi('pypynum')
        return x * 180 / pi_val
    elif backend_type == 'numpy':
        return backend.degrees(x)
    else:
        return x * 180 / math.pi


def power(base, exp, preferred_backend='auto'):
    """幂函数"""
    backend_type, backend = backend_manager.get_cmath_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.pow(base, exp)
    elif backend_type == 'numpy':
        return backend.power(base, exp)
    else:  # math or cmath
        if isinstance(base, complex) or isinstance(exp, complex) or base < 0 or base != base or exp != exp:
            return backend.pow(base, exp)
        else:
            return backend.pow(float(base), float(exp))


def abs_value(x, preferred_backend='auto'):
    """绝对值函数"""
    backend_type, backend = backend_manager.get_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        return backend.abs(x)
    elif backend_type == 'numpy':
        return backend.abs(x)
    else:
        return backend.fabs(x) if isinstance(x, float) and not isinstance(x, complex) else backend.abs(x)


# 重要常量
def get_pi(preferred_backend='auto'):
    """获取π值"""
    backend_type, backend = backend_manager.get_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        # 使用mp_pi函数获取高精度π值
        try:
            return float(backend.mp_pi())
        except:
            # 如果mp_pi不可用，尝试其他方法
            try:
                return float(backend.pi(100, 1000, lambda x: x if x > 0 else -x))
            except:
                # 如果pypynum不可用，返回math.pi
                return math.pi
    elif backend_type == 'numpy':
        return backend.pi
    else:
        return backend.pi


def get_e(preferred_backend='auto'):
    """获取e值"""
    backend_type, backend = backend_manager.get_backend(preferred_backend)
    
    if backend_type == 'pypynum':
        # 使用mp_e函数获取高精度e值
        try:
            if hasattr(backend, 'mp_e'):
                return float(backend.mp_e())
            else:
                return float(backend.exp(1))
        except:
            # 如果pypynum不可用或没有相应函数，返回math.e
            return math.e
    elif backend_type == 'numpy':
        return backend.e
    else:
        return backend.e


# 检查可用的后端
def available_backends():
    """返回可用的后端列表"""
    result = []
    if backend_manager.backends['pypynum']:
        result.append('pypynum')
    if backend_manager.backends['numpy']:
        result.append('numpy')
    result.append('math')
    result.append('cmath')
    return result