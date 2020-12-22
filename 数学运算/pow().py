# pow(base, exp[, mod])

# pow power exp exponent mod module

# 返回 base 的 exp 次幂；如果 mod 存在，则返回 base 的 exp 次幂对 mod 取余（比 pow(base, exp) % mod 更高效）。 两参数形式 pow(base, exp) 等价于乘方运算符: base**exp。

# 返回 base 的 exp 次幂；
print(f'{ pow(2, 3) = }')
print(f'{ pow(10, 2) = }')
# 两参数形式 pow(base, exp) 等价于乘方运算符: base**exp。
print(f'{ 2**3 = }')
print(f'{ 10**2 = }')
# 如果 mod 存在，则返回 base 的 exp 次幂对 mod 取余（比 pow(base, exp) % mod 更高效）
# 如果mod存在，会使用快速幂取模的算法来取模
import time
start = time.time()
print(f'{ pow(1234, 1234567, 67) = }')
end = time.time()
print(f' 耗时：{ end - start = } ')
# start = time.time()
# print(f'{ pow(1234, 1234567) % 67 = }')
# end = time.time()
# print(f' 耗时：{ end - start = } ')
#
# 参数必须具有数值类型。 对于混用的操作数类型，则将应用双目算术运算符的类型强制转换规则。 对于 int 操作数，结果具有与操作数相同的类型（强制转换后），除非第二个参数为负值；在这种情况下，所有参数将被转换为浮点数并输出浮点数结果。 例如，10**2 返回 100，但 10**-2 返回 0.01。

# 参数必须具有数值类型
# print(f'{ pow(2, "3") = }')
# 对于混用的操作数类型，则将应用双目算术运算符的类型强制转换规则。
print(f'{ pow(2.0, 3) = }')
# 对于 int 操作数，结果具有与操作数相同的类型（强制转换后），除非第二个参数为负值；在这种情况下，所有参数将被转换为浮点数并输出浮点数结果。
print(f'{ pow(2, 3) = }')
print(f'{ pow(2, -3) = }')
#
# 对于 int 操作数 base 和 exp，如果给出 mod，则 mod 必须为整数类型并且 mod 必须不为零。 如果给出 mod 并且 exp 为负值，则 base 必须相对于 mod 不可整除。 在这种情况下，将会返回 pow(inv_base, -exp, mod)，其中 inv_base 为 base 的倒数对 mod 取余。
#

# 对于 int 操作数 base 和 exp，如果给出 mod，则 mod 必须为整数类型并且 mod 必须不为零。
# print(f'{ pow(2, 3, 0) = }')

# 下面的例子是 38 的倒数对 97 取余:
#
# >>>
# >>> pow(38, -1, mod=97)
# 23
# >>> 23 * 38 % 97 == 1
# True
# 在 3.8 版更改: 对于 int 操作数，三参数形式的 pow 现在允许第二个参数为负值，即可以计算倒数的余数。
#
# 在 3.8 版更改: 允许关键字参数。 之前只支持位置参数。