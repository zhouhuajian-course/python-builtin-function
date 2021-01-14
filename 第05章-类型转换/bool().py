# class bool([x])
# 返回一个布尔值，True 或者 False。 x 使用标准的 真值测试过程 来转换。如果 x 是假的或者被省略，返回 False；其他情况返回 True。bool 类是 int 的子类（参见 数字类型 --- int, float, complex）。其他类不能继承自它。它只有 False 和 True 两个实例（参见 布尔值）。

# 返回一个布尔值，True 或者 False。 x 使用标准的 真值测试过程 来转换。如果 x 是假的或者被省略，返回 False；
print(f'{ bool() = }')
print(f'{ bool(None) = }')
print(f'{ bool(False) = }')

from decimal import Decimal
from fractions import Fraction
print(f'{ bool(0) = }')
print(f'{ bool(0.0) = }')
print(f'{ bool(0j) = }')
print(f'{ bool(Decimal(0)) = }')
print(f'{ bool(Fraction(0, 1)) = }')
print('-'*20)
print(f'{ bool("") = }')
print(f'{ bool(()) = }')
print(f'{ bool([]) = }')
print(f'{ bool({}) = }')
print(f'{ bool(set()) = }')
print(f'{ bool(range(0)) = }')
# 如果 x 是假的或者被省略，返回 False；其他情况返回 True。
print(f'{ bool(123) = }')
print(f'{ bool(1.23) = }')
print(f'{ bool("test") = }')
#
# bool 类是 int 的子类（参见 数字类型 --- int, float, complex）。其他类不能继承自它
print(f'{ issubclass(bool, int) = }')
# class C(bool):
#     pass

# 在 3.7 版更改: x 现在只能作为位置参数。