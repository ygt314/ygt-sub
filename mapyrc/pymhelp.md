# Pym Mathematical Calculator / 数学计算器

## Basic Usage / 基本用法
```bash
pym "expression" [scale]    # scale: decimal places / 小数位数
pym "2+2"                   # Output/输出: 4
pym "1/3" 4                 # Output/输出: 0.3333 (4 decimals/四位小数)
```

## Commands / 命令

↓Command/命令↓ ↓Description/说明↓
`quit` or `exit` Exit program / 退出程序
`clear` Clear screen / 清屏
`set x = 1` Assign variable / 变量赋值
`-h` or `--help` [name] Show help / 显示帮助

## Mathematical Constants / 数学常数

↓Symbol/符号↓Meaning/含义↓Approx Value/近似值↓
`pi` π 3.1415926535...
`e` Natural constant / 自然常数 e 2.7182818284...
`phi` Golden ratio φ / 黄金分割比 0.6180339887...
`s2` √2 1.4142135623...
`gama` Euler's constant γ / 欧拉常数 0.5772156649...
`i` Imaginary unit / 虚数单位 √-1

## Trigonometric Functions / 三角函数

↓Function/函数↓Description/说明↓Example/示例↓
`sin(x)` Sine (radians) / 正弦(弧度) sin(pi/2) → 1
`sin(x, deg)` Sine (degrees) / 正弦(角度) sin(30, deg) → 0.5
`cos(x)` Cosine / 余弦 cos(pi) → -1
`tan(x)` Tangent / 正切 tan(pi/4) → 1
`cot(x)` Cotangent / 余切 cot(pi/4) → 1
`sec(x)` Secant / 正割 sec(0) → 1
`csc(x)` Cosecant / 余割 csc(pi/2) → 1

## Inverse Trigonometric Functions / 反三角函数

↓Function/函数↓Description/说明↓Return value/返回值↓
`asin(x)` Arcsin / 反正弦 radians/弧度
`acos(x)` Arccos / 反余弦 radians/弧度
`atan(x)` Arctan / 反正切 radians/弧度
`acot(x)` Arccot / 反余切 radians/弧度
`asec(x)` Arcsec / 反正割 radians/弧度
`acsc(x)` Arccsc / 反余割 radians/弧度

## Angle Conversion / 角度转换

↓Function/函数↓Description/说明↓Example/示例↓
`d\_r(degrees)` Degrees → Radians / 度→弧度 d_r(180) → 3.14159...
`r_d(radians)` Radians → Degrees / 弧度→度 r\_d(pi) → 180

## Hyperbolic Functions / 双曲函数

↓Function/函数↓ ↓Description/说明↓
`sinh(x)` Hyperbolic sine / 双曲正弦
`cosh(x)` Hyperbolic cosine / 双曲余弦
`tanh(x)` Hyperbolic tangent / 双曲正切
`asinh(x)` Inverse hyperbolic sine / 反双曲正弦
`acosh(x)` Inverse hyperbolic cosine / 反双曲余弦
`atanh(x)` Inverse hyperbolic tangent / 反双曲正切

## Other Functions / 其他函数

↓Function/函数↓ ↓Description/说明↓
`sqrt(x)` Square root / 平方根
`cbrt(x)` Cube root / 立方根
`log(x)` Natural log / 自然对数
`lg(x)` Base-10 log / 常用对数
`abs(x)` Absolute value / 绝对值
`floor(x)` Round down / 向下取整
`ceil(x)` Round up / 向上取整
`ma.[func]()` More math functions / 更多数学函数

## Format Functions / 格式化函数

↓Function/函数↓ ↓Description/说明↓
`xsex(n, cale=12)` Simplify decimals / 简化小数
`cn_rn(c, cale=12)` Try to get real number / 尝试得到实数

# Examples / 示例

## Basic Arithmetic / 基础运算

```python
2 + 4          # Addition/加法 → 6
56 - 45        # Subtraction/减法 → 11
13 * 15        # Multiplication/乘法 → 195
345 / 5        # Division/除法 → 69
2 ** 3         # Power/幂 (2³) → 8
8 ** (1/3)     # Cube root/立方根 → 2
```

## Complex Numbers / 复数运算

```python
(-1) ** 0.5    # Square root/平方根 → 1j
1j ** 2        # Complex square/复数平方 → -1
(2+3j) + (1-2j)  # Complex addition/复数加法 → 3+1j
```

## Trigonometry / 三角函数

```python
sin(pi/2)          # 1
sin(30, deg)       # 0.5 (30 degrees/30度)
cos(pi)            # -1
tan(pi/4)          # 1
asin(1)            # 1.5708... (π/2 radians/弧度)
r_d(asin(1))       # 90 (degrees/度)
```

## Variables / 变量使用

```python
set x = 5
set y = 3
x * y + 2          # → 17
```

## Using math module / 使用数学模块

```python
ma.factorial(5)    # 120
ma.gcd(12, 8)      # 4
ma.comb(5, 2)      # 10 (combinations/组合数)
```

# Important Notes / 重要提示

## ⚠️ Rules / 规则

1. Use quotes for expressions with parentheses
   带括号的表达式必须用引号
   ```bash
   # Wrong/错误
   pym sin(30)
   
   # Correct/正确
   pym "sin(30)"
   ```
2. Complex numbers use j notation
   a+bi复数用 `a+[b]j` 表示
   ```python
   1+2j    # Complex number/复数
   3j      # Imaginary number/纯虚数
   ```
3. Variables are single letters a-z
   变量为单个字母 a-z
   ```python
   set a = 10
   set b = 20
   a + b    # → 30
   ```
4. Use `ma.` prefix for more math functions
   使用 `ma.` 前缀调用更多函数
   ```python
   ma.perm(5, 2)    # Permutations/排列数
   ma.gamma(5)      # Gamma function/伽马函数
   ```

## 🚫 Security Restrictions / 安全限制

· No os module access / 不能访问 os 模块
· No import statements / 不能使用 import 语句
· No double underscores \__ / 不能使用双下划线

# Quick Reference Card / 快速参考卡

## Most Used / 最常用

```python
# Constants/常数
pi, e, i

# Basic/基础
+, -, *, /, **, ()

# Trig/三角函数
sin(x), cos(x), tan(x)

# Convert/转换
d_r(180), r_d(pi)

# Format/格式化
"expression" [scale]
```

## Error Messages / 错误信息

Message/信息 Meaning/含义
"[notice]:can't use os or import" Security violation/安全违规
"SyntaxError Expression" error/表达式错误

## Exit / 退出

· Type quit or exit to leave / 输入 quit 或 exit 退出
· Type clear to clean screen / 输入 clear 清屏

---

# Happy Calculating! / 计算愉快！
