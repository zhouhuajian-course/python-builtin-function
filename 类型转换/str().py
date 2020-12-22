# class str(object='')
# class str(object=b'', encoding='utf-8', errors='strict')
# 返回 object 的 字符串 版本。 如果未提供 object 则返回空字符串。
print(f'{ str() = }')

# 在其他情况下 str() 的行为取决于 encoding 或 errors 是否有给出，具体见下。
# 如果 encoding 或 errors 均未给出，str(object) 返回 object.__str__()，这是 object 的“非正式”或格式良好的字符串表示。 对于字符串对象，这是该字符串本身。 如果 object 没有 __str__() 方法，则 str() 将回退为返回 repr(object)。
print(f'{ str(123) = }')
print(f'{ str([1, 2, 3]) = }')
print(f'{ str(range(3)) = }')
print(f'{ str("test") = }')
print('------')
class C:
    # def __str__(self):
    #     return "测试1"
    def __repr__(self):
        return "测试2"
print(f'{ str(C()) = }')


#
# 如果 encoding 或 errors 至少给出其中之一，则 object 应该是一个 bytes-like object (例如 bytes 或 bytearray)。 在此情况下，如果 object 是一个 bytes (或 bytearray) 对象，则 str(bytes, encoding, errors) 等价于 bytes.decode(encoding, errors)。 否则的话，会在调用 bytes.decode() 之前获取缓冲区对象下层的 bytes 对象。 请参阅 二进制序列类型 --- bytes, bytearray, memoryview 与 缓冲协议 了解有关缓冲区对象的信息。

# 如果 encoding 或 errors 至少给出其中之一，则 object 应该是一个 bytes-like object (例如 bytes 或 bytearray)。 在此情况下，如果 object 是一个 bytes (或 bytearray) 对象，则 str(bytes, encoding, errors) 等价于 bytes.decode(encoding, errors)。
print('-------')
# print(f'{ str("test", encoding="utf-8") = }')
bytes_object = bytes("test", "utf-8")
bytearray_object = bytearray("test", "utf-8")
print(f'{ str(bytes_object, encoding="utf-8") = }')
print(f'{ str(bytearray_object, encoding="utf-8", errors="strict") = }')
print(f'{ bytes_object.decode("utf-8") = }')
print(f'{ bytearray_object.decode("utf-8", "strict") = }')

# 将一个 bytes 对象传入 str() 而不给出 encoding 或 errors 参数的操作属于第一种情况， 将返回非正式的字符串表示（另请参阅 Python 的 -b 命令行选项）。 例如:
#
# >>>
# >>> str(b'Zoot!')
# "b'Zoot!'"
# 有关 str 类及其方法的更多信息，请参阅下面的 文本序列类型 --- str 和 字符串的方法 小节。 要输出格式化字符串，请参阅 格式化字符串字面值 和 格式字符串语法 小节。 此外还可以参阅 文本处理服务 小节。