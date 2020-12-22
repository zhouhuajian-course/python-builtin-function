# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# 返回一个新的字典，基于可选的位置参数和可能为空的关键字参数集来初始化。
#
# 字典可用多种方式来创建:
#
# 使用花括号内以逗号分隔 键: 值 对的方式: {'jack': 4098, 'sjoerd': 4127} or {4098: 'jack', 4127: 'sjoerd'}
#
# 使用字典推导式: {}, {x: x ** 2 for x in range(10)}
#
# 使用类型构造器: dict(), dict([('foo', 100), ('bar', 200)]), dict(foo=100, bar=200)
#
# 返回一个新的字典，基于可选的位置参数和可能为空的关键字参数集来初始化。

# 如果没有给出位置参数，将创建一个空字典。
print(f'{ dict() = }')

# 如果给出一个位置参数并且其属于映射对象，将创建一个具有与映射对象相同键值对的字典。
print(f'{ dict({"one": 1, "two": 2, "three": 3}) = }')
# 否则的话，位置参数必须为一个 iterable 对象。
# 该可迭代对象中的每一项本身必须为一个刚好包含两个元素的可迭代对象。
# 每一项中的第一个对象将成为新字典的一个键，第二个对象将成为其对应的值。
print(f'{ dict([("one", 1), ("two", 2), ("three", 3)]) = }')
# print(f'{ dict([("one", 1, "test"), ("two", 2), ("three", 3)]) = }')
# 如果一个键出现一次以上，该键的最后一个值将成为其在新字典中对应的值。
print(f'{ dict([("one", 11), ("two", 2), ("three", 3), ("one", 111), ("one", 1)]) = }')
#
# 如果给出了关键字参数，则关键字参数及其值会被加入到基于位置参数创建的字典。
# 如果要加入的键已存在，来自关键字参数的值将替代来自位置参数的值。
print(f'{ dict(one=1, two=2, three=3) = }')
print(f'{ dict({"two": 2, "three": 3}, one=1) = }')
print(f'{ dict({"one": 11, "two": 2, "three": 3}, one=1) = }')
#
# 作为演示，以下示例返回的字典均等于 {"one": 1, "two": 2, "three": 3}:
#
# >>>
# >>> a = dict(one=1, two=2, three=3)
# >>> b = {'one': 1, 'two': 2, 'three': 3}
# >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
# >>> e = dict({'three': 3, 'one': 1, 'two': 2})
# >>> f = dict({'one': 1, 'three': 3}, two=2)
# >>> a == b == c == d == e == f
# True
# 像第一个例子那样提供关键字参数的方式只能使用有效的 Python 标识符作为键。 其他方式则可使用任何有效的键。