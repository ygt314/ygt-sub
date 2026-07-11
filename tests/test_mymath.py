"""
测试基线：mymath.py（核心枢纽）+ mymath_real.py（回退导出 shim）
覆盖全部公开 API，锁定重构前行为
"""
import pytest
from pytest import approx
import math


# ============================================================
# 导入 mymath 模块（会触发 pypynum 抑制和 math_adapter 初始化）
# ============================================================
import mymath
import mymath_real


# ============================
# 全局常量和变量
# ============================
class TestConstants:
    def test_pi(self):
        assert mymath.pi == approx(3.141592653589793, rel=1e-15)

    def test_e(self):
        assert mymath.e == approx(2.718281828459045, rel=1e-15)

    def test_s2(self):
        assert mymath.s2 == approx(1.4142135623730951, rel=1e-15)

    def test_phi(self):
        assert mymath.phi == approx(0.6180339887498949, rel=1e-15)

    def test_gama(self):
        assert mymath.gama == approx(0.5772156649015328606, rel=1e-15)

    def test_i(self):
        assert mymath.i == 1j


# ============================
# 角度转换
# ============================
class TestAngleConversion:
    def test_d_r_180(self):
        """180° = π rad"""
        assert mymath.d_r(180) == approx(math.pi, rel=1e-15)

    def test_d_r_90(self):
        """90° = π/2 rad"""
        assert mymath.d_r(90) == approx(math.pi / 2, rel=1e-15)

    def test_d_r_0(self):
        assert mymath.d_r(0) == approx(0, abs=1e-15)

    def test_r_d_pi(self):
        """π rad = 180°"""
        assert mymath.r_d(math.pi) == approx(180, rel=1e-15)

    def test_r_d_pi_over_2(self):
        """π/2 rad = 90°"""
        assert mymath.r_d(math.pi / 2) == approx(90, rel=1e-15)

    def test_r_d_0(self):
        assert mymath.r_d(0) == approx(0, abs=1e-15)


# ============================
# 数值工具
# ============================
class TestNumUtils:
    def test_num_int(self):
        assert mymath.num(3) is True

    def test_num_float(self):
        assert mymath.num(3.14) is True

    def test_num_complex(self):
        assert mymath.num(3 + 4j) is True

    def test_num_str(self):
        assert mymath.num("abc") is False

    def test_num_list(self):
        assert mymath.num([1, 2]) is False

    def test_cn_rn_no_op(self):
        """已实数的复数应返回实部"""
        assert mymath.cn_rn(3 + 0j) == 3

    def test_cn_rn_clean_imag(self):
        """微小虚部应被清洗"""
        result = mymath.cn_rn(3 + 1e-15j, cale=12)
        assert isinstance(result, float)
        assert result == approx(3, abs=1e-12)

    def test_cn_rn_preserve_large_imag(self):
        """有效虚部应保留"""
        result = mymath.cn_rn(3 + 4j)
        assert result == 3 + 4j

    def test_xsex_no_change_for_int(self):
        assert mymath.xsex(3) == 3

    def test_xsex_complex_real(self):
        """复数实部近似整数时返回实部"""
        result = mymath.xsex(3.0 + 0j)
        assert result == approx(3, abs=1e-10)

    def test_xsex_imag_clean(self):
        """虚部很小但实部为0时返回虚部"""
        result = mymath.xsex(1e-12j * 1j)  # 接近0+0j
        # 当实部接近0时返回虚部形式
        assert hasattr(result, 'imag')


# ============================
# 连分数（分数形式）
# ============================
class TestFraction:
    def test_confs_half(self):
        """0.5 -> 1/2"""
        assert mymath.confs(0.5) == "1/2"

    def test_confs_third(self):
        """1/3 -> 1/3"""
        result = mymath.confs(1/3, cale=6)
        assert result == "1/3"

    def test_confs_integer(self):
        """整数直接返回字符串"""
        assert mymath.confs(2.0) == "2"

    def test_confs_negative(self):
        """负数连分数"""
        result = mymath.confs(-0.5)
        assert result == "-1/2"


# ============================
# 三角函数
# ============================
class TestTrig:
    def test_sin_0(self):
        assert mymath.sin(0) == approx(0, abs=1e-15)

    def test_sin_pi_over_2(self):
        assert mymath.sin(mymath.pi / 2) == approx(1, abs=1e-15)

    def test_sin_pi(self):
        assert mymath.sin(mymath.pi) == approx(0, abs=1e-15)

    def test_sin_deg_90(self):
        assert mymath.sin(90, mymath.deg) == approx(1, abs=1e-15)

    def test_cos_0(self):
        assert mymath.cos(0) == approx(1, abs=1e-15)

    def test_cos_pi(self):
        assert mymath.cos(mymath.pi) == approx(-1, abs=1e-15)

    def test_cos_pi_over_2(self):
        assert mymath.cos(mymath.pi / 2) == approx(0, abs=1e-15)

    def test_tan_0(self):
        assert mymath.tan(0) == approx(0, abs=1e-15)

    def test_tan_pi_over_4(self):
        assert mymath.tan(mymath.pi / 4) == approx(1, rel=1e-15)

    def test_cot_pi_over_4(self):
        assert mymath.cot(mymath.pi / 4) == approx(1, rel=1e-15)

    def test_sec_0(self):
        assert mymath.sec(0) == approx(1, abs=1e-15)

    def test_csc_pi_over_2(self):
        assert mymath.csc(mymath.pi / 2) == approx(1, abs=1e-15)


# ============================
# 反三角函数
# ============================
class TestInverseTrig:
    def test_asin_1(self):
        assert mymath.asin(1) == approx(mymath.pi / 2, rel=1e-15)

    def test_asin_0(self):
        assert mymath.asin(0) == approx(0, abs=1e-15)

    def test_acos_1(self):
        assert mymath.acos(1) == approx(0, abs=1e-15)

    def test_acos_0(self):
        assert mymath.acos(0) == approx(mymath.pi / 2, rel=1e-15)

    def test_atan_1(self):
        assert mymath.atan(1) == approx(mymath.pi / 4, rel=1e-15)

    def test_atan_0(self):
        assert mymath.atan(0) == approx(0, abs=1e-15)

    def test_acot_1(self):
        assert mymath.acot(1) == approx(mymath.pi / 4, rel=1e-15)

    def test_asec_1(self):
        assert mymath.asec(1) == approx(0, abs=1e-15)

    def test_acsc_1(self):
        assert mymath.acsc(1) == approx(mymath.pi / 2, rel=1e-15)

    def test_asin_deg(self):
        """角度制输出"""
        assert mymath.asin(1, mymath.deg) == approx(90, rel=1e-15)


# ============================
# 双曲函数
# ============================
class TestHyperbolic:
    def test_sinh_0(self):
        assert mymath.sinh(0) == approx(0, abs=1e-15)

    def test_cosh_0(self):
        assert mymath.cosh(0) == approx(1, abs=1e-15)

    def test_tanh_0(self):
        assert mymath.tanh(0) == approx(0, abs=1e-15)

    def test_asinh_0(self):
        assert mymath.asinh(0) == approx(0, abs=1e-15)

    def test_acosh_1(self):
        assert mymath.acosh(1) == approx(0, abs=1e-15)

    def test_atanh_0(self):
        assert mymath.atanh(0) == approx(0, abs=1e-15)


# ============================
# 数学工具函数
# ============================
class TestMathUtils:
    def test_sqrt_4(self):
        assert mymath.sqrt(4) == approx(2, rel=1e-15)

    def test_sqrt_2(self):
        assert mymath.sqrt(2) == approx(math.sqrt(2), rel=1e-15)

    def test_cbrt_8(self):
        assert mymath.cbrt(8) == approx(2, rel=1e-15)

    def test_cbrt_27(self):
        assert mymath.cbrt(27) == approx(3, rel=1e-15)

    def test_exp_0(self):
        assert mymath.exp(0) == approx(1, abs=1e-15)

    def test_exp_1(self):
        assert mymath.exp(1) == approx(mymath.e, rel=1e-15)

    def test_lg_100(self):
        assert mymath.lg(100) == approx(2, rel=1e-15)

    def test_lg_1(self):
        assert mymath.lg(1) == approx(0, abs=1e-15)

    def test_ln_e(self):
        assert mymath.ln(mymath.e) == approx(1, abs=1e-15)

    def test_ln_1(self):
        assert mymath.ln(1) == approx(0, abs=1e-15)

    def test_log_base_10(self):
        """对数的底数为10"""
        assert mymath.log(100, 10) == approx(2, rel=1e-15)

    @pytest.mark.xfail(strict=True, reason="math_adapter: cmath 无 log2 方法，base=2 触发 AttributeError")
    def test_log_base_2(self):
        """对数的底数为2（已知问题：cmath.log2 不存在）"""
        assert mymath.log(8, 2) == approx(3, rel=1e-15)

    def test_floor(self):
        assert mymath.floor(3.14) == 3
        assert mymath.floor(-3.14) == -4
        assert mymath.floor(5.0) == 5

    def test_ceil(self):
        assert mymath.ceil(3.14) == 4
        assert mymath.ceil(-3.14) == -3
        assert mymath.ceil(5.0) == 5


# ============================
# 安全过滤
# ============================
class TestSecurity:
    def test_able_safe_expr(self):
        """纯数学表达式应通过"""
        assert mymath.able_("1+1") is True

    def test_able_safe_func(self):
        """安全函数应通过"""
        assert mymath.able_("sin(pi)") is True

    def test_able_block_import(self):
        """import 应被拦截"""
        assert mymath.able_("import os") is False

    def test_able_block_exec(self):
        """exec 应被拦截"""
        assert mymath.able_("exec('print(1)')") is False

    def test_able_block_eval(self):
        """eval 应被拦截"""
        assert mymath.able_("eval('1+1')") is False

    def test_able_block_open(self):
        """open 应被拦截"""
        assert mymath.able_("open('/etc/passwd')") is False

    def test_able_block_dunder(self):
        """双下划线魔术方法应被拦截"""
        assert mymath.able_("__import__('os')") is False

    def test_able_block_os(self):
        """os 模块应被拦截"""
        assert mymath.able_("os.system('ls')") is False


# ============================
# 数列函数
# ============================
class TestSequence:
    def test_an_single(self):
        """a_n = n, n=5 -> 5"""
        assert mymath.an("n", 5) == 5

    def test_an_range(self):
        """a_n = n^2, n=1..5 -> [1,4,9,16,25]"""
        assert mymath.an("n**2", 1, 5) == [1, 4, 9, 16, 25]

    def test_dn_single(self):
        """d_n = n^2, n=2 -> a_2 - a_1 = 4-1 = 3"""
        assert mymath.dn("n**2", 2) == 3

    def test_dn_range(self):
        assert mymath.dn("n**2", 1, 3) == [1, 3, 5]

    def test_sn_single(self):
        """S_n for a_n=n, n=3 -> 1+2+3=6"""
        assert mymath.sn("n", 3) == 6

    def test_sn_range(self):
        """S_1..3 for a_n=n -> [1, 3, 6]"""
        result = mymath.sn("n", 1, 3)
        assert result == [1, 3, 6]


# ============================
# 表达式求值
# ============================
class TestEval:
    def test_mmpy_basic(self):
        assert mymath.mmpy("1+1") == 2

    def test_mmpy_pi(self):
        result = mymath.mmpy("pi")
        assert result == approx(mymath.pi, rel=1e-12)

    def test_mmpy_sin_pi_over_2(self):
        result = mymath.mmpy("sin(pi/2)")
        assert result == approx(1, abs=1e-12)

    def test_mpy_basic(self):
        assert mymath.mpy("1+1") == 2

    def test_mpy_precision(self):
        """mpy 默认 16 位精度"""
        result = mymath.mpy("pi")
        assert result == approx(mymath.pi, rel=1e-15)

    def test_mpy_euler_identity(self):
        """欧拉恒等式 e^(πi) + 1 = 0"""
        result = mymath.mmpy("e**(pi*i)+1")
        assert result == approx(0, abs=1e-12)


# ============================
# 实复模式开关
# ============================
class TestRealMode:
    def setup_method(self):
        # 保存原始状态
        self._orig_real_mode = mymath.real_mode

    def teardown_method(self):
        # 恢复原始状态，避免干扰后续测试
        mymath.real_mode = self._orig_real_mode

    def test_real_mode_default_false(self):
        """默认复数模式"""
        assert mymath.real_mode is False

    def test_getrn_real(self):
        """getrn 应返回实部"""
        assert mymath.getrn(3 + 0j) == 3.0

    def test_getrn_complex(self):
        """getrn 对复数只取实部"""
        assert mymath.getrn(3 + 4j) == 3.0

    def test_getfs_half(self):
        """getfs(0.5) -> 1/2"""
        assert mymath.getfs(0.5) == "1/2"

    def test_real_mode_on(self):
        """real_mode=True 时 mmpy 返回实数"""
        mymath.real_mode = True
        result = mymath.mmpy("sin(pi/2) + 0j")
        assert isinstance(result, float)
        assert result == approx(1, abs=1e-12)

    def test_real_mode_off(self):
        """real_mode=False 时 mmpy 可返回复数"""
        mymath.real_mode = False
        result = mymath.mmpy("1+2j")
        assert isinstance(result, complex)


# ============================
# mymath_real.py 回退导出 shim
# ============================
class TestRealShim:
    def test_shim_imports_exist(self):
        """mymath_real 应导出所声明的全部名称"""
        assert hasattr(mymath_real, 'getrn')
        assert hasattr(mymath_real, 'getfs')
        assert hasattr(mymath_real, 'mmpy')
        assert hasattr(mymath_real, 'mpy')
        assert hasattr(mymath_real, 'real_mode')

    def test_shim_getrn_identical(self):
        """mymath_real.getrn 与 mymath.getrn 相同"""
        assert mymath_real.getrn is mymath.getrn

    def test_shim_getfs_identical(self):
        assert mymath_real.getfs is mymath.getfs

    def test_shim_mmpy_identical(self):
        assert mymath_real.mmpy is mymath.mmpy

    def test_shim_mpy_identical(self):
        assert mymath_real.mpy is mymath.mpy

    def test_shim_real_mode_identical(self):
        assert mymath_real.real_mode is mymath.real_mode

    def test_shim_getrn_works(self):
        """mymath_real.getrn 功能正常"""
        assert mymath_real.getrn(3 + 0j) == 3.0

    def test_shim_mmpy_works(self):
        """mymath_real.mmpy 功能正常"""
        assert mymath_real.mmpy("1+1") == 2


# ============================
# Euler's identity (来自 mymath.py 的 __main__ 块)
# ============================
class TestEulerIdentity:
    def test_euler_identity(self):
        """欧拉恒等式 e^(iπ) + 1 = 0 (使用mmpy调用)"""
        ans = mymath.cn_rn(eval("e**(pi*i)+1", mymath.__dict__))
        assert ans == approx(0, abs=1e-12)


# ============================
# 公式字符串 (来自 formula_str 的导入验证)
# ============================
class TestFormulaStrImports:
    """验证 mymath.py 底部的 from formula_str import * 生效"""

    def test_validate_formula_exists(self):
        assert hasattr(mymath, 'validate_formula')

    def test_eval_formula_exists(self):
        assert hasattr(mymath, 'eval_formula')


# ============================
# myfunc 导入验证
# ============================
class TestMyfuncImports:
    """验证 mymath.py 底部的 from myfunc import * 生效"""

    def test_fx_exists(self):
        assert hasattr(mymath, 'fx')

    def test_lim_exists(self):
        assert hasattr(mymath, 'lim')
