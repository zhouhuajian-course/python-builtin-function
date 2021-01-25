# oct(x)
# 将一个整数转变为一个前缀为“0o”的八进制字符串。结果是一个合法的 Python 表达式。如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数。一些例子：

# 将一个整数转变为一个前缀为“0o”的八进制字符串。
print(f'{ oct(8) = }')
print(f'{ oct(-8) = }')
print(f'{ oct(0) = }')
print(f'{ oct(0b111) = }')
print(f'{ oct(0o177) = }')
print(f'{ oct(0x7f) = }')
# 结果是一个合法的 Python 表达式。
print(f'{ oct(8) = } { eval(oct(8)) = } { eval("0o10") = }')
# 如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数。
# class C:
#     pass
# print(f'{ oct(C()) = }')
class C:
    def __index__(self):
        return 127
print(f'{ oct(C()) = }')

#
# >>>
# oct(8)
# '0o10'
# oct(-56)
# '-0o70'
# 如果要将整数转换为八进制字符串，并可选择有无“0o”前缀，则可以使用如下方法：
#
# >>>
# '%#o' % 10, '%o' % 10
# ('0o12', '12')
# format(10, '#o'), format(10, 'o')
# ('0o12', '12')
# f'{10:#o}', f'{10:o}'
# ('0o12', '12')
# 另见 format() 获取更多信息。