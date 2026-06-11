'''
Formula String Expression
公式字符串表达与处理
(by YGT&AI)
功能：提供公式字符串的解析、格式化、求值等功能
'''

from mymath import *
from myfunc import get_fx, fx
import random,re
# 常量定义
op_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '**': 3}
op_associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R', '**': 'R'}

# 字符串处理基础函数
def is_operator(c):
    '''判断是否为运算符'''
    return c in '+-*/^'

def is_function(name):
    '''判断是否为函数名'''
    functions = ['sin', 'cos', 'tan', 'cot', 'sec', 'csc',
                 'asin', 'acos', 'atan', 'acot', 'asec', 'acsc',
                 'sinh', 'cosh', 'tanh', 'asinh', 'acosh', 'atanh',
                 'sqrt', 'cbrt', 'exp', 'log', 'lg', 'ln',
                 'abs', 'floor', 'ceil', 'round']
    return name in functions

def is_constant(name):
    '''判断是否为常量名'''
    constants = ['pi', 'e', 'i', 'phi', 'gama', 's2', 'inf', 's']
    return name in constants

def format_formula(f, precision=6):
    '''格式化公式字符串'''
    f = f.replace(' ', '')
    # 简化连续运算符
    f = f.replace('+-', '-')
    f = f.replace('-+', '-')
    f = f.replace('--', '+')
    return f

# 公式验证与安全检查
def validate_formula(f):
    '''验证公式字符串的合法性'''
    if not f or not isinstance(f, str):
        return False, "公式不能为空"
    # 使用able_函数进行安全检查
    if not able_(f):
        return False, "公式包含不安全内容"
    # 括号匹配检查
    stack = []
    for i, ch in enumerate(f):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if not stack:
                return False, f"括号不匹配: 位置{i}处多余的')'"
            stack.pop()
    if stack:
        return False, f"括号不匹配: 缺少{len(stack)}个')'"
    return True, "公式合法"

# 公式解析与求值
def eval_formula(f,vars_dict=None,_round=True):
    '''安全地求值公式字符串'''
    # 验证公式
    valid, msg = validate_formula(f)
    if not valid:
        raise ValueError(f"公式验证失败: {msg}")
    # 准备变量字典
    if vars_dict is None:
        vars_dict = {}
    # 合并全局变量
    eval_dict = {
        'pi': pi, 'e': e, 'i': i, 'phi': phi, 'gama': gama, 's2': s2,
        'inf': inf, 's': s,
        'sin': sin, 'cos': cos, 'tan': tan, 'cot': cot, 'sec': sec, 'csc': csc,
        'asin': asin, 'acos': acos, 'atan': atan, 'acot': acot, 'asec': asec, 'acsc': acsc,
        'sinh': sinh, 'cosh': cosh, 'tanh': tanh,
        'asinh': asinh, 'acosh': acosh, 'atanh': atanh,
        'sqrt': sqrt, 'cbrt': cbrt, 'exp': exp, 'log': log, 'lg': lg, 'ln': ln,
        'abs': abs, 'floor': floor, 'ceil': ceil,
        'r_d': r_d, 'd_r': d_r
    }
    eval_dict.update(vars_dict)
    try:
        result = eval(f, {"__builtins__": {}}, eval_dict)
        return cn_rn(result) if _round else result
    except Exception as ex:
        raise ValueError(f"公式求值失败: {ex}")

def formula_to_function(f, var_name='x'):
    '''将公式字符串转换为函数'''
    valid, msg = validate_formula(f)
    if not valid:
        raise ValueError(f"公式验证失败: {msg}")
    # 使用myfunc的get_fx
    return get_fx(f)

# 公式简化与变换
def simplify_formula(f):
    '''简化公式（基本代数简化）'''
    # 尝试求值常量部分
    try:
        # 分割表达式为项
        # 这是一个简化的实现
        result = eval_formula(f)
        if isinstance(result, (int, float)) and abs(result - int(result)) < 1e-10:
            return str(int(result))
        elif isinstance(result, (int, float)):
            return str(result)
    except:
        pass
    return f

def expand_formula(f):
    '''展开公式（如乘法分配律）'''
    # 这是一个占位函数，实际实现需要更复杂的代数系统
    return f

def factor_formula(f):
    '''因式分解公式'''
    # 这是一个占位函数
    return f

# 公式比较与匹配
def formulas_equal(f1, f2, test_points=10):
    '''检查两个公式是否等价（通过数值测试）'''
    # 转换为函数
    try:
        func1=formula_to_function(f1)
        func2=formula_to_function(f2)
    except:
        return False
    # 随机测试点
    for _ in range(test_points):
        x = random.uniform(-10, 10)
        try:
            y1 = func1(x)
            y2 = func2(x)
            if abs(cn_rn(y1 - y2,9))>0:
                return False
        except Exception as ex:
            raise ValueError(f"函数求值失败: {ex}")
    return True

# 公式模板
class FormulaTemplate:
    '''公式模板类，用于生成特定类型的公式'''
    def __init__(self, template_str):
        self.template = template_str
        self.variables = self._extract_variables(template_str)
    def _extract_variables(self, template):
        '''提取模板中的变量（形如 {name}）'''
        return list(set(re.findall(r'\{([^}]+)\}', template)))
    def render(self, **kwargs):
        '''渲染模板'''
        result = self.template
        for var in self.variables:
            if var in kwargs:
                value = kwargs[var]
                # 格式化数值
                if isinstance(value, (int, float, complex)):
                    if isinstance(value, complex):
                        value_str = xs_fs(value)
                    else:
                        value_str = str(cn_rn(value, 10))
                else:
                    value_str = str(value)
                result = result.replace(f'{{{var}}}', value_str)
        return result

# 常用公式模板
common_templates = {
    'quadratic': '{a}x^2 + {b}x + {c}',  # 二次方程
    'line': '{k}x + {b}', # 直线
    'sinusoid': '{A}sin({omega}x + {phi})', # 正弦波
    'exponential': '{a} * e^({k}x)', # 指数函数
    'logarithm': '{a} * log({b}x + {c})', # 对数函数
    'power': '{a} * x^{n}', # 幂函数
    'rational': '({p})/({q})', # 有理函数
}

def get_template(name):
    '''获取常用公式模板'''
    if name in common_templates:
        return FormulaTemplate(common_templates[name])
    return None

# 公式解析为中缀/后缀表达式
def infix_to_postfix(infix):
    '''中缀表达式转后缀表达式（逆波兰表示法）'''
    output = []
    stack = []
    tokens = infix.replace(' ', '')
    i = 0
    while i < len(tokens):
        token = tokens[i]
        # 处理数字
        if token.isdigit() or token == '.':
            j = i
            while j < len(tokens) and (tokens[j].isdigit() or tokens[j] == '.'):
                j += 1
            output.append(tokens[i:j])
            i = j
            continue
        # 处理变量和函数
        elif token.isalpha():
            j = i
            while j < len(tokens) and (tokens[j].isalnum() or tokens[j] == '_'):
                j += 1
            name = tokens[i:j]
            if is_function(name):
                stack.append(name)
            else:
                output.append(name)
            i = j
            continue
        # 处理运算符
        elif token in '+-*/^':
            while (stack and stack[-1] in '+-*/^' and
                   ((op_associativity.get(token, 'L') == 'L' and 
                     op_priority.get(token, 0) <= op_priority.get(stack[-1], 0)) or
                    (op_associativity.get(token, 'L') == 'R' and 
                     op_priority.get(token, 0) < op_priority.get(stack[-1], 0)))):
                output.append(stack.pop())
            stack.append(token)
        # 处理括号
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            if stack and is_function(stack[-1]):
                output.append(stack.pop())
        i += 1
    while stack:
        output.append(stack.pop())
    return output

def evaluate_postfix(postfix, vars_dict=None):
    '''计算后缀表达式'''
    stack = []
    for token in postfix:
        if token in '+-*/^':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
        elif is_function(token):
            arg = stack.pop()
            # 调用对应的函数
            func_map = {
                'sin': sin, 'cos': cos, 'tan': tan,
                'sqrt': sqrt, 'exp': exp, 'log': log,
                'abs': abs, 'floor': floor, 'ceil': ceil
            }
            if token in func_map:
                stack.append(func_map[token](arg))
            else:
                raise ValueError(f"未知函数: {token}")
        else:
            # 尝试转换为数值
            try:
                if token.endswith('j') or 'j' in token:
                    stack.append(complex(token))
                elif '.' in token:
                    stack.append(float(token))
                else:
                    stack.append(int(token))
            except:
                # 可能是变量
                if vars_dict and token in vars_dict:
                    stack.append(vars_dict[token])
                else:
                    # 尝试使用全局变量
                    try:
                        stack.append(eval(token, {'pi': pi, 'e': e, 'i': i}))
                    except:
                        stack.append(0)  # 默认值
    return stack[0] if stack else 0

# 公式字符串格式化输出
def pretty_print_formula(f, width=80):
    '''美化打印公式'''
    # 替换运算符为更美观的形式
    f = f.replace('*', '·')
    f = f.replace('sqrt', '√')
    f = f.replace('pi', 'π')
    f = f.replace('**', '^')
    # 处理分数形式
    import re
    f = re.sub(r'\(([^)]+)\)/([^)]+)', r'┌\1┐\n---\n└\2┘', f)
    return f

# 公式解析树
class FormulaNode:
    '''公式节点类（抽象语法树节点）'''
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.node_type = self._determine_type(value)
    def _determine_type(self, value):
        if isinstance(value, (int, float, complex)):
            return 'number'
        elif is_operator(value):
            return 'operator'
        elif is_function(value):
            return 'function'
        else:
            return 'variable'
    def evaluate(self, vars_dict=None):
        '''计算节点值'''
        if self.node_type == 'number':
            return self.value
        elif self.node_type == 'variable':
            if vars_dict and self.value in vars_dict:
                return vars_dict[self.value]
            return 0
        elif self.node_type == 'operator':
            left_val = self.left.evaluate(vars_dict) if self.left else 0
            right_val = self.right.evaluate(vars_dict) if self.right else 0
            ops = {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b,
                '^': lambda a, b: a ** b
            }
            return ops[self.value](left_val, right_val)
        elif self.node_type == 'function':
            arg_val = self.left.evaluate(vars_dict) if self.left else 0
            funcs = {
                'sin': sin, 'cos': cos, 'tan': tan,
                'sqrt': sqrt, 'exp': exp, 'log': log,
                'abs': abs
            }
            return funcs[self.value](arg_val)
    def __str__(self):
        if self.node_type in ['number', 'variable']:
            return str(self.value)
        elif self.node_type == 'function':
            return f"{self.value}({self.left})"
        else:
            return f"({self.left} {self.value} {self.right})"

def build_parse_tree(infix):
    '''从公式构建解析树'''
    # 使用后缀表达式构建树
    postfix = infix_to_postfix(infix)
    stack = []
    for token in postfix:
        if token in '+-*/^':
            right = stack.pop()
            left = stack.pop()
            stack.append(FormulaNode(token, left, right))
        elif is_function(token):
            arg = stack.pop()
            stack.append(FormulaNode(token, arg, None))
        else:
            # 尝试转换为数值
            try:
                if token.endswith('j') or 'j' in token:
                    stack.append(FormulaNode(complex(token)))
                elif '.' in token:
                    stack.append(FormulaNode(float(token)))
                else:
                    stack.append(FormulaNode(int(token)))
            except:
                stack.append(FormulaNode(token))
    return stack[0] if stack else None

# 单元测试
if __name__ == "__main__":
    # 测试公式验证
    print("=== 公式验证测试 ===")
    formulas = ["x+1", "sin(x)+cos(x)", "__import__('os')", "eval('print(1)')"]
    for f in formulas:
        valid, msg = validate_formula(f)
        print(f"'{f}': {valid} - {msg}")
    # 测试公式求值
    print("\n=== 公式求值测试 ===")
    test_formulas = ["pi*2", "sin(pi/2)", "e**(i*pi)+1", "sqrt(16)"]
    for f in test_formulas:
        try:
            result = eval_formula(f)
            print(f"{f} = {result}")
        except Exception as e:
            print(f"{f} 求值失败: {e}")
    # 测试公式模板
    print("\n=== 公式模板测试 ===")
    quad_template = get_template('quadratic')
    if quad_template:
        result = quad_template.render(a=2, b=3, c=1)
        print(f"二次方程模板: {result}")
    # 测试中缀转后缀
    print("\n=== 中缀转后缀测试 ===")
    infix = "3+4*2/(1-5)^2"
    postfix = infix_to_postfix(infix)
    print(f"中缀: {infix}")
    print(f"后缀: {' '.join(postfix)}")
    # 测试解析树
    print("\n=== 解析树测试 ===")
    tree = build_parse_tree("sin(x)+cos(x)")
    if tree:
        print(f"解析树: {tree}")
        # 在x=0处求值
        result = tree.evaluate({'x': 0})
        print(f"在x=0处求值: {cn_rn(result)}")
    # 测试公式等价性
    print("\n=== 公式等价性测试 ===")
    f1 = "(x+1)**2"
    f2 = "x*x+2*x+1"
    f3 = "x*x+2*x+2"
    print(f"'{f1}' 与 '{f2}' 等价: {formulas_equal(f1, f2)}")
    print(f"'{f1}' 与 '{f3}' 等价: {formulas_equal(f1, f3)}")
    print("\nformula_str 库初始化完成")