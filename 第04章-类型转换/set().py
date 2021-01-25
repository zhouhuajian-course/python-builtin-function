# class set([iterable])
# class frozenset([iterable])
# 返回一个新的 set 或 frozenset 对象，其元素来自于 iterable。 集合的元素必须为 hashable。 要表示由集合对象构成的集合，所有的内层集合必须为 frozenset 对象。 如果未指定 iterable，则将返回一个新的空集合。
#
# 返回一个新的 set 或 frozenset 对象，其元素来自于 iterable。
print(f'{ set(["a", "b", "c"]) = }')
print(f'{ set(["a", "b", "c", "a"]) = }')
print(f'{ set(("a", "b", "c")) = }')
print(f'{ set(range(3)) = }')
print(f'{ set("abc") = }')
# 如果未指定 iterable，则将返回一个新的空集合。
print('-------')
print(f'{ set() = }')

# 集合可用多种方式来创建:
#
# 使用花括号内以逗号分隔元素的方式: {'jack', 'sjoerd'}
#
# 使用集合推导式: {c for c in 'abracadabra' if c not in 'abc'}
#
# 使用类型构造器: set(), set('foobar'), set(['a', 'b', 'foo'])