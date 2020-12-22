# any(iterable)
# 如果 iterable 的任一元素为真值则返回 True。 如果可迭代对象为空，返回 False。 等价于:
#
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
from decimal import Decimal
from fractions import Fraction
# 如果 iterable 的任一元素为真值则返回 True。
iterable = [None, False, 0, 0.0, 0j, Decimal("0.0"), Fraction(0, 1), "test", (), [], {}, set(), range(0)]
print(f'{ any(iterable) = }')
# 如果可迭代对象为空，返回 False。
print(f'{ any([]) = }')
print(f'{ any(()) = }')
# 如果可迭代对象不为空，并且iterable的所有元素都为假值，则返回False
iterable = [None, False, 0, 0.0, 0j, Decimal("0.0"), Fraction(0, 1), "", (), [], {}, set(), range(0)]
print(f'{ any(iterable) = }')
