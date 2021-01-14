# filter(function, iterable)
# 用 iterable 中函数 function 返回真的那些元素，构建一个新的迭代器。iterable 可以是一个序列，一个支持迭代的容器，或一个迭代器。如果 function 是 None ，则会假设它是一个身份函数，即 iterable 中所有返回假的元素会被移除。

# 用 iterable 中函数 function 返回真的那些元素，构建一个新的迭代器。iterable 可以是一个序列，一个支持迭代的容器，或一个迭代器。
def func(elem):
    return elem in ['a', 'b', 'c', 'd', 'e']
print(f'{ filter(func, "apple") = }')
print(f'{ type(filter(func, "apple")) = }')
print(f'{ list(filter(func, "apple")) = }')
print(f'{ tuple(filter(func, "apple")) = }')
print(f'{ set(filter(func, "apple")) = }')
for elem in filter(func, "apple"):
    print(elem)
# iterable 可以是一个序列，一个支持迭代的容器，或一个迭代器。
def func(elem):
    return elem % 2 == 0
print(f'{ filter(func, [0, 1, 2, 3, 4, 5]) = }')
print(f'{ list(filter(func, [0, 1, 2, 3, 4, 5])) = }')
# iterable 可以是一个序列，一个支持迭代的容器，或一个迭代器。
def func(elem):
    return elem % 2 == 0
iterator = iter([0, 1, 2, 3, 4, 5])
print(f'{ filter(func, iterator) = }')
print(f'{ list(filter(func, iterator)) = }')
# 如果 function 是 None ，则会假设它是一个身份函数，即 iterable 中所有返回假的元素会被移除。
print(f'{ list(filter(None, [None, False, 0, 0.0, 1, "test", ""])) = }')
#
# 请注意， filter(function, iterable) 相当于一个生成器表达式，当 function 不是 None 的时候为 (item for item in iterable if function(item))；function 是 None 的时候为 (item for item in iterable if item) 。
#
# 请参阅 itertools.filterfalse() 了解，只有 function 返回 false 时才选取 iterable 中元素的补充函数