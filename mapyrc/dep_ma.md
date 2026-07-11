# mapyrc/ 依赖关系分析

## 文件清单（15 个 .py）

| 文件 | 角色 |
|------|------|
| `math_adapter.py` | 数学后端适配层 |
| `mymath.py` | **核心数学库** |
| `mymath_real.py` | 实数回退 shim |
| `myfunc.py` | 函数计算（导数/积分/泰勒） |
| `formula_str.py` | 公式字符串处理 |
| `math_extensions.py` | 加密/矩阵/图像/逻辑电路 |
| `math_txt.py` | 数学文本解析引擎 |
| `zmath.py` | 交互式 REPL |
| `zm-sh.py` | 命令行表达式求值器 |
| `tri_solve.py` | 三角形求解器（增强版） |
| `con_arr.py` | 组合数学 |
| `mv_pe.py` | 物理碰撞计算 |
| `nyht.py` | 高阶等差数列求和 |
| `sq_cal.py` | 平方根整数算法 |
| `sqrt_sh.py` | 平方根脚本包装器 |

---

## 依赖关系总图

```
math_adapter.py  ──外部──→  math, sys, os, warnings, io, contextlib
(后端适配层)     ──可选──→  pypynum, numpy
       │
       │ 提供 sin/cos/sqrt/exp/log/pi/e ...
       ▼
┌──────────────────────────────────────────────────────┐
│                   mymath.py                           │
│ 导入 math_adapter 所有函数, 包装后重新导出            │
│ 定义: d_r, r_d, cn_rn, xsex, confs, able_            │
│       real_mode, getrn, getfs, mmpy, mpy             │
│       an, dn, sn  (数列)                              │
│ 外部: sys, os, re, cmath                              │
│ 内部: ← formula_str, ← myfunc (文件末尾导入)         │
└────┬──────┬──────┬──────┬──────┬──────┬──────────────┘
     │      │      │      │      │      │
     ▼      ▼      ▼      ▼      ▼      ▼
  myfunc  formula  mymath  zmath  zm-sh  math_txt
  .py     _str.py  _real   .py    .py    .py
  导数/   公式解析  .py     REPL   命令行  文本解析
  积分/   中缀/     (shim)  交互   求值器  引擎
  泰勒    后缀      ↓
     │    转换     tri_solve.py
     │             三角形求解
     ▼             (from mymath_real *)
  tri_solve.py
  (from myfunc *)
```

---

## 各文件依赖明细

### math_adapter.py
- **外部依赖**: `math`, `sys`, `os`, `warnings`, `io`, `contextlib`
- **第三方(可选)**: `pypynum`, `numpy`
- **内部依赖**: 无
- **被谁导入**: `mymath.py`, `zmath.py`, `zm-sh.py`

### mymath.py （核心，被导入最多 — 10 次）
- **外部依赖**: `sys`, `os`, `re`, `cmath`
- **内部依赖**:
  - `from math_adapter import *`
  - `from formula_str import *`（文件末尾）
  - `from myfunc import *`（文件末尾）
- **被谁导入**:
  - **mapyrc 内**: `myfunc.py`, `formula_str.py`, `mymath_real.py`, `zmath.py`, `zm-sh.py`, `math_txt.py`
  - **mapyrc 外**: `plot.py`, `plot2.py`, `plot_sh.py`, `plot2_sh.py`, `sun_len.py`, `yfx.py`

### mymath_real.py （薄层 shim）
- **内部依赖**: `from mymath import getrn, getfs, mmpy, mpy, real_mode`
- **被谁导入**: `tri_solve.py`

### myfunc.py
- **内部依赖**: `from mymath import *`
- **被谁导入**: `mymath.py`, `formula_str.py`, `tri_solve.py`

### formula_str.py
- **外部依赖**: `random`, `re`
- **内部依赖**: `from mymath import *`, `from myfunc import get_fx, fx`
- **被谁导入**: `mymath.py`

### tri_solve.py
- **第三方(可选)**: `mpmath`
- **内部依赖**: `from mymath_real import *`, `from myfunc import *`
- **被谁导入**: `tri_abA.py`（mapyrc 外）

### 其余文件
| 文件 | 依赖 | 被谁导入 |
|------|------|---------|
| `zmath.py` | `math_adapter`, `mymath` | 无（入口脚本） |
| `zm-sh.py` | `math_adapter`, `mymath` | 无（入口脚本） |
| `math_txt.py` | `mymath`, `sympy`（按需） | 无 |
| `math_extensions.py` | `warnings`, `pypynum`（可选） | 无 |
| `con_arr.py` | `math`, `typing` | 无 |
| `mv_pe.py` | 无 | 无 |
| `nyht.py` | `sympy` | 无 |
| `sq_cal.py` | 无 | `sqrt_sh.py` |
| `sqrt_sh.py` | `sq_cal`, `sys` | 无（入口脚本） |

---

## 关键发现

### 1. 循环依赖（2 组）

```
循环 A: mymath.py  ←→  myfunc.py
循环 B: mymath.py  ←→  formula_str.py
```

**工作原理**: `mymath.py` 将 `from formula_str import *` 和 `from myfunc import *` 放在文件末尾（所有核心定义之后），所以被导入方使用时依赖已就绪。

### 2. tri_solve.py 自引用 bug

`tri_solve.py:11` 中存在 `from tri_solve import tgt, modA, sABC, ...` 自引用导入，将导致 `AttributeError`。文件内容本质上是增强版（`tri_solve_enhanced`），但文件名覆盖了原始 `tri_solve.py`。

### 3. 孤立模块（5 个，在 mapyrc 内未被引用）

- `con_arr.py` — 组合数学
- `mv_pe.py` — 物理碰撞
- `nyht.py` — 高阶等差求和
- `math_extensions.py` — 加密/矩阵/图像/逻辑
- `math_txt.py` — 数学文本解析

### 4. 第三方依赖

| 库 | 文件 | 是否必需 |
|-----|------|:--------:|
| `pypynum` | `math_adapter.py`, `math_extensions.py` | 可选 |
| `numpy` | `math_adapter.py` | 可选 |
| `sympy` | `math_txt.py`, `nyht.py` | 按需导入 |
| `mpmath` | `tri_solve.py` | 可选 |
| `readline` | `zmath.py` | 是 |

---

## 核心导入统计

| 文件 | mapyrc 内导入 | 外部导入 | 合计 |
|------|:-----------:|:--------:|:---:|
| **mymath.py** | 6 | 4 | **10** |
| **myfunc.py** | 3 | 1 | **4** |
| **math_adapter.py** | 3 | 0 | **3** |
| **mymath_real.py** | 1 | 1+ | **2+** |
| **formula_str.py** | 1 | 0 | **1** |
| **sq_cal.py** | 1 | 0 | **1** |
| **tri_solve.py** | 0 | 1 | **1** |
