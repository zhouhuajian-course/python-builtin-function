# chr(i)
# 返回 Unicode 码位为整数 i 的字符的字符串格式。例如，chr(97) 返回字符串 'a'，chr(8364) 返回字符串 '€'。这是 ord() 的逆函数。

# 返回 Unicode 码位为整数 i 的字符的字符串格式。
print(f'{ chr(10) = }')
print(f'{ chr(65) = }')
print(f'{ chr(97) = }')
print(f'{ chr(0xa9) = }')
print(f'{ chr(0x6c49) = }')
print(f'{ chr(0x1f60e) = }')
print(f'{ chr(0x1f408) = }')
# 这是 ord() 的逆函数。
print(f'{ chr(ord("🐈")) = }')

#
# 实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）。如果 i 超过这个范围，会触发 ValueError 异常。

# 实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）。如果 i 超过这个范围，会触发 ValueError 异常。
print(f'{ chr(0x10ffff) = }')
print(f'{ chr(0x10ffff + 0x1) = }')