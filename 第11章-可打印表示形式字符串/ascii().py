# ascii(object)
# 就像函数 repr()，返回一个对象可打印的字符串，但是 repr() 返回的字符串中非 ASCII 编码的字符，会使用 \x、\u 和 \U 来转义。生成的字符串和 Python 2 的 repr() 返回的结果相似。

# 就像函数 repr()，返回一个对象可打印的字符串，但是 repr() 返回的字符串中非 ASCII 编码的字符，会使用 \x、\u 和 \U 来转义。
print(f'{ ascii(123) = }')
print(f'{ repr(123) = }')
print(f'{ ascii(1.23) = }')
print(f'{ repr(1.23) = }')
print(f'{ ascii("test") = }')
print(f'{ repr("test") = }')
print(f'{ ascii([1, 2, 3]) = }')
print(f'{ repr([1, 2, 3]) = }')
# Unciode码点(码位、编号)
#     0~127 ASCII字符，不会使用\x \u \U转义字符
#     128~255 会使用\x转义字符
#     256~65535 会使用\u转义字符
#     65536~0x10ffff 会使用\U转义字符
print('---------')
print(f'{ ascii("test©汉😎") = }')
print(f'{ repr("test©汉😎") = }')
print(f'{ ascii(["test", "©", "汉", "😎"]) = }')
print(f'{ repr(["test", "©", "汉", "😎"]) = }')