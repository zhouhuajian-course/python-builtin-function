# class bytearray([source[, encoding[, errors]]])
# 返回一个新的 bytes 数组。 bytearray 类是一个可变序列，包含范围为 0 <= x < 256 的整数。它有可变序列大部分常见的方法，见 可变序列类型 的描述；同时有 bytes 类型的大部分方法，参见 bytes 和 bytearray 操作。
#
# 返回一个新的 bytes 数组。
# 可选形参 source 可以用不同的方式来初始化数组：
#
# 如果是一个 string，您必须提供 encoding 参数（errors 参数仍是可选的）；bytearray() 会使用 str.encode() 方法来将 string 转变成 bytes。
print(f'{ bytearray("test", "utf-8") = }')
print(f'{ type(bytearray("test", "utf-8")) = }')
print(f'{ "test".encode("utf-8") = }')
print(f'{ type("test".encode("utf-8")) = }')
print('-------------')
print(f'{ bytearray("test", "utf-8", "strict") = }')
print(f'{ "test".encode("utf-8", "strict") = }')
#
# 如果是一个 integer，会初始化大小为该数字的数组，并使用 null 字节填充。
print('--------------')
print(f'{ bytearray(3) = }')
#
# 如果是一个遵循 缓冲区接口 的对象，该对象的只读缓冲区将被用来初始化字节数组。
print('------------')
bytes_object = "test".encode("utf-8")
print(f'{ bytearray(bytes_object) = }')
#
# 如果是一个 iterable 可迭代对象，它的元素的范围必须是 0 <= x < 256 的整数，它会被用作数组的初始内容。
print('--------------')
print(f'{ bytearray([10, 65, 97, 98, 99]) = }')
# print(f'{ bytearray([256, 257]) = }')
#
# 如果没有实参，则创建大小为 0 的数组。
print('-----------------')
print(f'{ bytearray() = }')
#
# 另见 二进制序列类型 --- bytes, bytearray, memoryview 和 bytearray 对象