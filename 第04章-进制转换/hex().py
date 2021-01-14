# hex(x)
# 将整数转换为以“0x”为前缀的小写十六进制字符串。如果 x 不是 Python int 对象，则必须定义返回整数的 __index__() 方法。一些例子：
#
# 将整数转换为以“0x”为前缀的小写十六进制字符串。
print(f'{ hex(15) = }')
print(f'{ hex(-15) = }')
print(f'{ hex(0) = }')
print(f'{ hex(0b11111111) = }')
print(f'{ hex(0o20) = }')
print(f'{ hex(0x7f) = }')
# 如果 x 不是 Python int 对象，则必须定义返回整数的 __index__() 方法。
# class C:
#     pass
# print(f'{ hex(C()) = }')
class C:
    def __index__(self):
        return 65535
print(f'{ hex(C()) = }')


# >>>
# hex(255)
# '0xff'
# hex(-42)
# '-0x2a'
# 如果要将整数转换为大写或小写的十六进制字符串，并可选择有无“0x”前缀，则可以使用如下方法：
#
# >>>
# '%#x' % 255, '%x' % 255, '%X' % 255
# ('0xff', 'ff', 'FF')
# format(255, '#x'), format(255, 'x'), format(255, 'X')
# ('0xff', 'ff', 'FF')
# f'{255:#x}', f'{255:x}', f'{255:X}'
# ('0xff', 'ff', 'FF')
# 另见 format() 获取更多信息。
#
# 另请参阅 int() 将十六进制字符串转换为以 16 为基数的整数。
#
# 注解 如果要获取浮点数的十六进制字符串形式，请使用 float.hex() 方法。