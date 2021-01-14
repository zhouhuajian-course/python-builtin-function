# class memoryview(obj)
# 创建一个引用 obj 的 memoryview。 obj 必须支持缓冲区协议。 支持缓冲区协议的内置对象包括 bytes 和 bytearray。
#
print(f'{ memoryview(b"abcdef") = }')
print(f'{ memoryview(bytes("abcdef", "utf-8")) = }')
print(f'{ memoryview(bytearray("abcdef", "utf-8")) = }')
print('-------')
print(f'{ hasattr(memoryview, "__len__") = }')
print(f'{ hasattr(memoryview, "__getitem__") = }')
print('-----------')
print(f'{ memoryview(b"abcdef")[0] = }')
print(f'{ memoryview(b"abcdef")[1] = }')
print('-----------')
print(f'{ memoryview(b"abcdef")[0:3] = }')
print(f'{ bytes(memoryview(b"abcdef")[0:3]) = }')
# memoryview 具有 元素 的概念，即由原始对象 obj 所处理的基本内存单元。 对于许多简单类型例如 bytes 和 bytearray 来说，一个元素就是一个字节，但是其他的类型例如 array.array 可能有更大的元素。
#
# len(view) 与 tolist 的长度相等。 如果 view.ndim = 0，则其长度为 1。 如果 view.ndim = 1，则其长度等于 view 中元素的数量。 对于更高的维度，其长度等于表示 view 的嵌套列表的长度。 itemsize 属性可向你给出单个元素所占的字节数。
#
# memoryview 支持通过切片和索引访问其元素。 一维切片的结果将是一个子视图:
#
# >>>
# >>> v = memoryview(b'abcefg')
# >>> v[1]
# 98
# >>> v[-1]
# 103
# >>> v[1:4]
# <memory at 0x7f3ddc9f4350>
# >>> bytes(v[1:4])
# b'bce'
# 如果 format 是一个来自于 struct 模块的原生格式说明符，则也支持使用整数或由整数构成的元组进行索引，并返回具有正确类型的单个 元素。 一维内存视图可以使用一个整数或由一个整数构成的元组进行索引。 多维内存视图可以使用由恰好 ndim 个整数构成的元素进行索引，ndim 即其维度。 零维内存视图可以使用空元组进行索引。
#
# 这里是一个使用非字节格式的例子:
#
# >>>
# >>> import array
# >>> a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
# >>> m = memoryview(a)
# >>> m[0]
# -11111111
# >>> m[-1]
# 44444444
# >>> m[::2].tolist()
# [-11111111, -33333333]
# 如果下层对象是可写的，则内存视图支持一维切片赋值。 改变大小则不被允许:
#
# >>>
# >>> data = bytearray(b'abcefg')
# >>> v = memoryview(data)
# >>> v.readonly
# False
# >>> v[0] = ord(b'z')
# >>> data
# bytearray(b'zbcefg')
# >>> v[1:4] = b'123'
# >>> data
# bytearray(b'z123fg')
# >>> v[2:3] = b'spam'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: memoryview assignment: lvalue and rvalue have different structures
# >>> v[2:6] = b'spam'
# >>> data
# bytearray(b'z1spam')
# 由带有格式符号 'B', 'b' 或 'c' 的可哈希（只读）类型构成的一维内存视图同样是可哈希的。 哈希定义为 hash(m) == hash(m.tobytes()):
#
# >>>
# >>> v = memoryview(b'abcefg')
# >>> hash(v) == hash(b'abcefg')
# True
# >>> hash(v[2:4]) == hash(b'ce')
# True
# >>> hash(v[::-2]) == hash(b'abcefg'[::-2])
# True
# 在 3.3 版更改: 一维内存视图现在可以被切片。 带有格式符号 'B', 'b' 或 'c' 的一维内存视图现在是可哈希的。
#
# 在 3.4 版更改: 内存视图现在会自动注册为 collections.abc.Sequence
#
# 在 3.5 版更改: 内存视图现在可使用整数元组进行索引。