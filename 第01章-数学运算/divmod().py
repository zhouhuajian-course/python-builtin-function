"""
divmod(a, b)
它将两个（非复数）数字作为实参，并在执行整数除法时返回一对商和余数。对于混合操作数类型，适用双目算术运算符的规则。对于整数，结果和 (a // b, a % b) 一致。对于浮点数，结果是 (q, a % b) ，q 通常是 math.floor(a / b) 但可能会比 1 小。在任何情况下， q * b + a % b 和 a 基本相等；如果 a % b 非零，它的符号和 b 一样，并且 0 <= abs(a % b) < abs(b) 。
"""
# division和modulus两个单词的缩写
# 它将两个（非复数）数字作为实参，并在执行整数除法时返回一对商和余数
# 返回值一个包含商和余数的元组
# 对于整数，结果和 (a // b, a % b) 一致。
a = 20  # 被除数
b = 3   # 除数
print(f'{ divmod(a, b) = }')
print(f'{ (a//b, a%b) = }')
# 对于浮点数，结果是 (q, a % b) ，q 通常是 math.floor(a / b)
import math
a = 2.0  # 被除数
b = 0.3  # 除数
q = math.floor(a/b)
print(f'{ divmod(a, b) = }')
print(f'{ (q, a%b) = }')
# 在任何情况下， q * b + a % b 和 a 基本相等
