# class float([x])
# 返回从数字或字符串 x 生成的浮点数。
#
# 如果实参是字符串，则它必须是包含十进制数字的字符串，字符串前面可以有符号，之前也可以有空格。可选的符号有 '+' 和 '-' ； '+' 对创建的值没有影响。实参也可以是 NaN（非数字）、正负无穷大的字符串。确切地说，除去首尾的空格后，输入必须遵循以下语法：

# 如果实参是字符串，则它必须是包含十进制数字的字符串，字符串前面可以有符号，之前也可以有空格。可选的符号有 '+' 和 '-' ； '+' 对创建的值没有影响。
print(f'{ float("1.23") = }')
print(f'{ float("+1.23") = }')
print(f'{ float("-1.23") = }')
print(f'{ float("    -1.23") = }')
#
# 实参也可以是 NaN（非数字）、正负无穷大的字符串。确切地说，除去首尾的空格后，输入必须遵循以下语法：
# sign           ::=  "+" | "-"
# infinity       ::=  "Infinity" | "inf"
# nan            ::=  "nan"
# numeric_value  ::=  floatnumber | infinity | nan
# numeric_string ::=  [sign] numeric_value
# 这里， floatnumber 是 Python 浮点数的字符串形式，详见 浮点数字面值。字母大小写都可以，例如，“inf”、“Inf”、“INFINITY”、“iNfINity” 都可以表示正无穷大。
print(f'{ float("NaN") = }')
print(f'{ float("Inf") = }')
print(f'{ float("Infinity") = }')
print(f'{ float("-Infinity") = }')
#
# 另一方面，如果实参是整数或浮点数，则返回具有相同值（在 Python 浮点精度范围内）的浮点数。如果实参在 Python 浮点精度范围外，则会触发 OverflowError。

# 如果实参是整数或浮点数，则返回具有相同值（在 Python 浮点精度范围内）的浮点数。如果实参在 Python 浮点精度范围外，则会触发 OverflowError。
print(f'{ float(123) = }')
print(f'{ float(1.23) = }')

#
# 对于一个普通 Python 对象 x，float(x) 会委托给 x.__float__()。 如果 __float__() 未定义则将回退至 __index__()。
class C:
    # def __float__(self):
    #     return 1.23
    def __index__(self):
        return 123
print(f'{ float(C()) = }')
#
# 如果没有实参，则返回 0.0 。
print(f'{ float() = }')
#
# 例如:
#
# >>>
# >>> float('+1.23')
# 1.23
# >>> float('   -12345\n')
# -12345.0
# >>> float('1e-003')
# 0.001
# >>> float('+1E6')
# 1000000.0
# >>> float('-Infinity')
# -inf
# 数字类型 --- int, float, complex 描述了浮点类型。
#
# 在 3.6 版更改: 您可以使用下划线将代码文字中的数字进行分组。
#
# 在 3.7 版更改: x 现在只能作为位置参数。
#
# 在 3.8 版更改: 如果 __float__() 未定义则回退至 __index__()