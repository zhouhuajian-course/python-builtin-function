# class int([x])
# class int(x, base=10)
# 返回一个基于数字或字符串 x 构造的整数对象，或者在未给出参数时返回 0。 如果 x 定义了 __int__()，int(x) 将返回 x.__int__()。 如果 x 定义了 __index__()，它将返回 x.__index__()。 如果 x 定义了 __trunc__()，它将返回 x.__trunc__()。 对于浮点数，它将向零舍入。

# 返回一个基于数字或字符串 x 构造的整数对象，或者在未给出参数时返回 0。
print(f'{ int() = }')
print(f'{ int(123) = }')
print(f'{ int("123") = }')
# 如果 x 定义了 __int__()，int(x) 将返回 x.__int__()。 如果 x 定义了 __index__()，它将返回 x.__index__()。 如果 x 定义了 __trunc__()，它将返回 x.__trunc__()。
class C:
    # def __int__(self):
    #     return 1
    # def __index__(self):
    #     return 2
    def __trunc__(self):
        return 3
print('-------')
print(f'{ int(C()) = }')
# 对于浮点数，它将向零舍入。
print('---------')
print(f'{ int(12.345) = }')
print(f'{ int(12.789) = }')
#
# 如果 x 不是数字，或者有 base 参数，x 必须是字符串、bytes、表示进制为 base 的 整数字面值 的 bytearray 实例。该文字前可以有 + 或 - （中间不能有空格），前后可以有空格。一个进制为 n 的数字包含 0 到 n-1 的数，其中 a 到 z （或 A 到 Z ）表示 10 到 35。默认的 base 为 10 ，允许的进制有 0、2-36。2、8、16 进制的数字可以在代码中用 0b/0B 、 0o/0O 、 0x/0X 前缀来表示。进制为 0 将安照代码的字面量来精确解释，最后的结果会是 2、8、10、16 进制中的一个。所以 int('010', 0) 是非法的，但 int('010') 和 int('010', 8) 是合法的。

# 如果 x 不是数字，或者有 base 参数，x 必须是字符串、bytes、bytearray 实例。
print('-----------')
print(f'{ int("123") = }')
print(f'{ int(bytes("123", "utf-8")) = }')
print(f'{ int(bytearray("123", "utf-8")) = }')
# 该文字前可以有 + 或 - （中间不能有空格），前后可以有空格。
print('-------------')
print(f'{ int("+123") = }')
print(f'{ int("-123") = }')
print(f'{ int("    -123    ") = }')
# 默认的 base 为 10 ，允许的进制有 0、2-36。
print('-----')
print(f'{ int("10") = }')
print(f'{ int("10", base=10) = }')
print(f'{ int("10", base=2) = }')
print(f'{ int("10", base=16) = }')
# 2、8、16 进制的数字可以在代码中用 0b/0B 、 0o/0O 、 0x/0X 前缀来表示。
print('-----')
print(f'{ int("0b10", base=2) = }')
print(f'{ int("0o10", base=8) = }')
print(f'{ int("0x10", base=16) = }')
# 进制为 0 将安照代码的字面量来精确解释，最后的结果会是 2、8、10、16 进制中的一个。
print('-----')
print(f'{ int("10", base=0) = }')
print(f'{ int("0b10", base=0) = }')
print(f'{ int("0o10", base=0) = }')
print(f'{ int("0x10", base=0) = }')
#
# 整数类型定义请参阅 数字类型 --- int, float, complex 。
#
# 在 3.4 版更改: 如果 base 不是 int 的实例，但 base 对象有 base.__index__ 方法，则会调用该方法来获取进制数。以前的版本使用 base.__int__ 而不是 base.__index__。
#
# 在 3.6 版更改: 您可以使用下划线将代码文字中的数字进行分组。
#
# 在 3.7 版更改: x 现在只能作为位置参数。
#
# 在 3.8 版更改: 如果 __int__() 未定义则回退至 __index__()