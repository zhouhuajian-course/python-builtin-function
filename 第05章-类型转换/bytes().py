# class bytes([source[, encoding[, errors]]])
# 返回一个新的“bytes”对象， 是一个不可变序列，包含范围为 0 <= x < 256 的整数。bytes 是 bytearray 的不可变版本 - 它有其中不改变序列的方法和相同的索引、切片操作。
#
# 因此，构造函数的实参和 bytearray() 相同。

# 返回一个新的“bytes”对象，
# 构造函数的实参和 bytearray() 相同。
# 如果source参数是一个字符串，必须提供encoding参数
print(f'{ bytes("test", "utf-8") = }')
print(f'{ type(bytes("test", "utf-8")) = }')
# 如果source是一个整型，会初始化大小为该数字的数组，并使用null字节填充
print('--------')
print(f'{ bytes(3) = }')
# 如果source是一个遵循 缓冲区接口 的对象，该对象的只读缓存区将被用来初始化字节数组
print('----------')
bytearray_object = bytearray('test', 'utf-8')
print(f'{ bytes(bytearray_object) = }')
#
# 如果source参数是一个iterable可迭代对象，它会被用作数组的初始化内容
print('------')
print(f'{ bytes([65, 66, 67]) = }')
# 如果没有实参，则创建大小为0的数组
print('------')
print(f'{ bytes() = }')
# 字节对象还可以用字面值创建，参见 字符串和字节串字面值。

# 字节对象还可以用字面值创建
print('---------')
print(f'{ bytes("test", "utf-8") = }')
print(f'{ b"test" = }')
print(f'{ type(b"test") = }')
#
# 另见 二进制序列类型 --- bytes, bytearray, memoryview，bytes 对象 和 bytes 和 bytearray 操作。