"""
combinatorial mathematics
组合数学计算

n! = n * (n-1) * ... * 2 * 1
阶乘

A(n, m): Arrangement
排列数：从 n 个不同元素中取出 m 个元素的所有排列个数
计算公式：A(n, m) = n! / (n-m)!

C(n, m): Combination
组合数：从 n 个不同元素中取出 m 个元素的所有组合个数
计算公式：C(n, m) = n! / (m! * (n-m)!)

B(n): Binomial Theorem
二项式定理展开系数：B(n) 表示 (a + b)^n 的系数列表
计算公式：B(n) = [C(n, 0), C(n, 1), ..., C(n, n)]
"""

import math
from typing import List, Union

# 阶乘
def factorial(n: int) -> int:
    """
    计算 n 的阶乘 n!
    Args:
        n: 非负整数
    Returns:
        n 的阶乘结果
    Raises:
        ValueError: 当 n 为负数时
    """
    if n < 0:
        raise ValueError("阶乘要求 n >= 0")
    return math.factorial(n)

# 排列数
def A(n: int, m: int) -> int:
    """
    计算排列数 A(n, m) = n! / (n-m)!
    Args:
        n: 总数，非负整数
        m: 选取个数，非负整数且满足 m <= n
    Returns:
        排列数
    Raises:
        ValueError: 当参数不满足条件时
    """
    if n < 0 or m < 0:
        raise ValueError("n 和 m 必须为非负整数")
    if m > n:
        raise ValueError("排列数要求 m <= n")
    # 使用 math.perm 直接计算排列数（Python 3.8+）
    return math.perm(n, m)

# 组合数
def C(n: int, m: int) -> int:
    """
    计算组合数 C(n, m) = n! / (m! * (n-m)!)
    Args:
        n: 总数，非负整数
        m: 选取个数，非负整数且满足 m <= n
    Returns:
        组合数
    Raises:
        ValueError: 当参数不满足条件时
    """
    if n < 0 or m < 0:
        raise ValueError("n 和 m 必须为非负整数")
    if m > n:
        raise ValueError("组合数要求 m <= n")
    # 使用 math.comb 直接计算组合数（Python 3.8+）
    return math.comb(n, m)

# 二项式定理系数
def B(n: int) -> List[int]:
    """
    计算二项式定理展开系数 B(n) = [C(n, 0), C(n, 1), ..., C(n, n)]
    Args:
        n: 非负整数，表示二项式的指数
    Returns:
        长度为 n+1 的系数列表
    Raises:
        ValueError: 当 n 为负数时
    """
    if n < 0:
        raise ValueError("二项式指数 n 必须为非负整数")
    return [math.comb(n, k) for k in range(n + 1)]

# 如果直接运行此文件，可以执行一些简单测试
if __name__ == "__main__":
    print("阶乘 5! =", factorial(5))
    print("排列 A(5, 3) =", A(5, 3))
    print("组合 C(5, 3) =", C(5, 3))
    print("二项式系数 B(5) =", B(5))