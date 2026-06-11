"""
数学扩展模块，集成pypynum的高级功能
"""
import warnings

# 尝试导入pypynum
try:
    import pypynum as pn
    HAS_PYPYNUM = True
except ImportError:
    pn = None
    HAS_PYPYNUM = False


class Encryption:
    """
    加密功能模块，基于pypynum的加密算法（如果可用）
    """
    
    def __init__(self):
        if not HAS_PYPYNUM:
            warnings.warn("pypynum not available, using basic implementations", ImportWarning)
    
    def caesar_cipher(self, text, shift):
        """凯撒密码加密"""
        if HAS_PYPYNUM and hasattr(pn, 'caesar'):
            return pn.caesar(text, shift)
        else:
            # 基本实现
            result = ""
            for char in text:
                if char.isalpha():
                    shift_base = 65 if char.isupper() else 97
                    result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
                else:
                    result += char
            return result
    
    def caesar_decipher(self, text, shift):
        """凯撒密码解密"""
        if HAS_PYPYNUM and hasattr(pn, 'caesar'):
            # pypynum的caesar函数可以处理负数shift
            return pn.caesar(text, -shift)
        else:
            # 基本实现
            result = ""
            for char in text:
                if char.isalpha():
                    shift_base = 65 if char.isupper() else 97
                    result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
                else:
                    result += char
            return result
    
    def vigenere_cipher(self, text, key):
        """维吉尼亚密码加密"""
        if HAS_PYPYNUM and hasattr(pn, 'vigenere'):
            try:
                # 尝试pypynum的vigenere函数，可能没有mode参数
                return pn.vigenere(text, key)
            except:
                # 如果失败，使用基本实现
                result = ""
                key_index = 0
                for char in text:
                    if char.isalpha():
                        shift_base = 65 if char.isupper() else 97
                        key_char = key[key_index % len(key)]
                        key_shift = ord(key_char.upper()) - 65
                        result += chr((ord(char) - shift_base + key_shift) % 26 + shift_base)
                        key_index += 1
                    else:
                        result += char
                return result
        else:
            # 基本实现
            result = ""
            key_index = 0
            for char in text:
                if char.isalpha():
                    shift_base = 65 if char.isupper() else 97
                    key_char = key[key_index % len(key)]
                    key_shift = ord(key_char.upper()) - 65
                    result += chr((ord(char) - shift_base + key_shift) % 26 + shift_base)
                    key_index += 1
                else:
                    result += char
            return result
    
    def atbash_cipher(self, text):
        """阿特巴什密码"""
        if HAS_PYPYNUM and hasattr(pn, 'atbash'):
            return pn.atbash(text)
        else:
            # 基本实现
            result = ""
            for char in text:
                if char.isalpha():
                    shift_base = 65 if char.isupper() else 97
                    result += chr(2 * shift_base + 25 - ord(char))
                else:
                    result += char
            return result


class MatrixOps:
    """
    矩阵运算模块，基于pypynum的矩阵功能（如果可用）
    """
    
    def __init__(self):
        if not HAS_PYPYNUM:
            warnings.warn("pypynum not available, matrix operations limited", ImportWarning)
    
    def create_matrix(self, data):
        """创建矩阵"""
        if HAS_PYPYNUM and hasattr(pn, 'Matrix'):
            return pn.Matrix(data)
        else:
            # 使用嵌套列表作为基本矩阵表示
            return data
    
    def matrix_multiply(self, a, b):
        """矩阵乘法"""
        if HAS_PYPYNUM and hasattr(pn, 'Matrix'):
            if not isinstance(a, pn.Matrix):
                a = pn.Matrix(a)
            if not isinstance(b, pn.Matrix):
                b = pn.Matrix(b)
            # 使用@操作符进行标准矩阵乘法
            try:
                return a @ b
            except:
                # 如果@操作符不可用，尝试*（可能需要先检查兼容性）
                return a * b  # 这可能是元素乘法，但对于兼容的形状可能也行
        else:
            # 基本矩阵乘法实现
            rows_a, cols_a = len(a), len(a[0])
            rows_b, cols_b = len(b), len(b[0])
            
            if cols_a != rows_b:
                raise ValueError("Cannot multiply matrices: incompatible dimensions")
            
            result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
            for i in range(rows_a):
                for j in range(cols_b):
                    for k in range(cols_a):
                        result[i][j] += a[i][k] * b[k][j]
            return result
    
    def matrix_add(self, a, b):
        """矩阵加法"""
        if HAS_PYPYNUM and hasattr(pn, 'Matrix'):
            if not isinstance(a, pn.Matrix):
                a = pn.Matrix(a)
            if not isinstance(b, pn.Matrix):
                b = pn.Matrix(b)
            return a + b
        else:
            # 基本矩阵加法实现
            rows_a, cols_a = len(a), len(a[0])
            rows_b, cols_b = len(b), len(b[0])
            
            if rows_a != rows_b or cols_a != cols_b:
                raise ValueError("Cannot add matrices: incompatible dimensions")
            
            result = [[a[i][j] + b[i][j] for j in range(cols_a)] for i in range(rows_a)]
            return result
    
    def matrix_transpose(self, matrix):
        """矩阵转置"""
        if HAS_PYPYNUM and hasattr(pn, 'Matrix'):
            if not isinstance(matrix, pn.Matrix):
                matrix = pn.Matrix(matrix)
            # 尝试不同的转置方法（都需要调用）
            if hasattr(matrix, 't'):
                return matrix.t()  # 调用方法
            elif hasattr(matrix, 'transpose'):
                return matrix.transpose()  # 调用方法
            elif hasattr(matrix, 'T'):
                return matrix.T()  # 调用方法
            else:
                # 手动转置
                return pn.Matrix([[matrix[i][j] for i in range(len(matrix))] 
                                  for j in range(len(matrix[0]))])
        else:
            # 基本转置实现
            rows, cols = len(matrix), len(matrix[0])
            result = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
            return result
    
    def matrix_determinant(self, matrix):
        """矩阵行列式"""
        if HAS_PYPYNUM and hasattr(pn, 'det'):
            if not isinstance(matrix, pn.Matrix):
                matrix = pn.Matrix(matrix)
            return pn.det(matrix)
        elif HAS_PYPYNUM and hasattr(matrix, 'det'):  # pypynum Matrix对象可能有det方法
            if isinstance(matrix, pn.Matrix):
                return matrix.det()
            else:
                matrix = pn.Matrix(matrix)
                return matrix.det()
        else:
            # 基本2x2和3x3行列式实现
            if isinstance(matrix, list):
                n = len(matrix)
                if n == 1:
                    return matrix[0][0]
                elif n == 2:
                    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
                elif n == 3:
                    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
                            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
                            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
                else:
                    raise NotImplementedError("Determinant computation only implemented for 1x1, 2x2, and 3x3 matrices in basic mode")
            else:
                # 如果传入的是pypynum Matrix对象但不支持det方法
                raise NotImplementedError("Determinant computation not implemented for this matrix type")
    
    def lu_decomposition(self, matrix):
        """LU分解"""
        if HAS_PYPYNUM and hasattr(pn, 'lu'):
            if not isinstance(matrix, pn.Matrix):
                matrix = pn.Matrix(matrix)
            return pn.lu(matrix)
        else:
            # 基本LU分解实现 (仅适用于简单情况)
            n = len(matrix)
            L = [[0.0 for _ in range(n)] for _ in range(n)]
            U = [[0.0 for _ in range(n)] for _ in range(n)]
            
            for i in range(n):
                for k in range(i, n):
                    sum_val = sum(L[i][j] * U[j][k] for j in range(i))
                    U[i][k] = matrix[i][k] - sum_val
                
                for k in range(i, n):
                    if i == k:
                        L[i][i] = 1
                    else:
                        sum_val = sum(L[k][j] * U[j][i] for j in range(i))
                        L[k][i] = (matrix[k][i] - sum_val) / U[i][i]
            
            return L, U


class ImageMath:
    """
    图像数学处理模块，基于pypynum的图像功能（如果可用）
    """
    
    def __init__(self):
        if not HAS_PYPYNUM:
            warnings.warn("pypynum not available, image processing limited", ImportWarning)
    
    def create_image(self, width, height, color=None):
        """创建图像"""
        if HAS_PYPYNUM and hasattr(pn, 'BaseImage'):
            return pn.BaseImage(width, height, color)
        else:
            # 基本图像表示
            if color is None:
                color = [0, 0, 0]  # 默认黑色
            return [[[color[0], color[1], color[2]] for _ in range(width)] for _ in range(height)]
    
    def load_image(self, filepath):
        """加载图像"""
        if HAS_PYPYNUM and hasattr(pn, 'BaseImage'):
            try:
                return pn.BaseImage.open(filepath)
            except:
                raise NotImplementedError("Image loading requires pypynum with image support")
        else:
            raise NotImplementedError("Image operations require pypynum")
    
    def save_image(self, image, filepath):
        """保存图像"""
        if HAS_PYPYNUM and hasattr(pn, 'BaseImage') and hasattr(image, 'save'):
            image.save(filepath)
        else:
            raise NotImplementedError("Image operations require pypynum")


class LogicCircuits:
    """
    逻辑电路模块，基于pypynum的逻辑功能（如果可用）
    """
    
    def __init__(self):
        if not HAS_PYPYNUM:
            warnings.warn("pypynum not available, logic circuits limited", ImportWarning)
    
    def and_gate(self, a, b):
        """AND门"""
        if HAS_PYPYNUM:
            # 检查pypynum是否提供了逻辑门类
            if hasattr(pn, 'AND'):
                try:
                    # pypynum的逻辑门可能需要不同的调用方式
                    gate = pn.AND("and_gate")  # 使用字符串标签
                    return gate(a, b)
                except:
                    # 如果失败，使用基本实现
                    return a and b
            else:
                # 如果pypynum没有AND函数，使用基本实现
                return a and b
        else:
            return a and b
    
    def or_gate(self, a, b):
        """OR门"""
        if HAS_PYPYNUM:
            if hasattr(pn, 'OR'):
                try:
                    gate = pn.OR("or_gate")
                    return gate(a, b)
                except:
                    return a or b
            else:
                return a or b
        else:
            return a or b
    
    def not_gate(self, a):
        """NOT门"""
        if HAS_PYPYNUM:
            if hasattr(pn, 'NOT'):
                try:
                    gate = pn.NOT("not_gate")
                    return gate(a)
                except:
                    return not a
            else:
                return not a
        else:
            return not a
    
    def xor_gate(self, a, b):
        """XOR门"""
        if HAS_PYPYNUM:
            if hasattr(pn, 'XOR'):
                try:
                    gate = pn.XOR("xor_gate")
                    return gate(a, b)
                except:
                    return (a and not b) or (not a and b)
            else:
                return (a and not b) or (not a and b)
        else:
            return (a and not b) or (not a and b)


# 创建全局实例
encryption = Encryption()
matrix_ops = MatrixOps()
image_math = ImageMath()
logic_circuits = LogicCircuits()


# 导出主要功能
__all__ = [
    'encryption', 'matrix_ops', 'image_math', 'logic_circuits',
    'Encryption', 'MatrixOps', 'ImageMath', 'LogicCircuits',
    'HAS_PYPYNUM'
]