# bin(x)
# 将一个整数转变为一个前缀为“0b”的二进制字符串。结果是一个合法的 Python 表达式。如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数。一些例子：

# 将一个整数转变为一个前缀为“0b”的二进制字符串。
print(f'{ bin(3) = }')
print(f'{ bin(-3) = }')
print(f'{ bin(0) = }')
print(f'{ bin(0b11) = }')
print(f'{ bin(0o10) = }')
print(f'{ bin(0x7f) = }')
# 结果是一个合法的 Python 表达式。
print(f'{ bin(3) = } { eval(bin(3)) = } { eval("0b11") = }')
# 如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数。
# class C:
#     pass
# print(f'{ bin(C()) = }')
class C:
    def __index__(self):
        return 2
print(f'{ bin(C()) = }')
#
# >>>
# bin(3)
# '0b11'
# bin(-10)
# '-0b1010'
# 如果不一定需要前缀“0b”，还可以使用如下的方法。
#
# >>>
# format(14, '#b'), format(14, 'b')
# ('0b1110', '1110')
# f'{14:#b}', f'{14:b}'
# ('0b1110', '1110')
# 另见 format() 获取更多信息。