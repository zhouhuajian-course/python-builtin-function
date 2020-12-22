# all(iterable)
# 如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True 。 等价于:
#
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
# 如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True 。
from decimal import Decimal
from fractions import Fraction
print(f'{ all([True, 123, 1.23, "test"]) = }')
print(f'{ all([(1, 2), [1, 2], {"name": "小明"}, {"a", "b"}, range(3)]) = }')
print(f'{ all([1+2j, Decimal("1.23"), Fraction(1, 2)]) = }')
print(f'{ all([]) = }')
print(f'{ all(()) = }')
# 如果可迭代对象不为空，只要有一个元素为假值，则返回False
print(f'{ all([True, 123, 1.23, ""]) = }')
print(f'{ all([(), [1, 2], {"name": "小明"}, {"a", "b"}, range(3)]) = }')
print(f'{ all([1+2j, Decimal("0.0"), Fraction(1, 2)]) = }')