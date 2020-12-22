# map(function, iterable, ...)
# 返回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器。 如果传入了额外的 iterable 参数，function 必须接受相同个数的实参并被应用于从所有可迭代对象中并行获取的项。 当有多个可迭代对象时，最短的可迭代对象耗尽则整个迭代就将结束。 对于函数的输入已经是参数元组的情况，请参阅 itertools.starmap()。

# 返回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器。
def func(elem):
    return elem**2
print(f'{ map(func, [1, 2, 3]) = }')
print(f'{ list(map(func, [1, 2, 3])) = }')
print(f'{ tuple(map(func, [1, 2, 3])) = }')
print(f'{ set(map(func, [1, 2, 3])) = }')
for elem in map(func, [1, 2, 3]):
    print(elem)
# 如果传入了额外的 iterable 参数，function 必须接受相同个数的实参并被应用于从所有可迭代对象中并行获取的项。
def func(iterable1_elem, iterable2_elem):
    return iterable1_elem + iterable2_elem
print(f'{ map(func, [1, 2, 3], [4, 5, 6]) = }')
print(f'{ list(map(func, [1, 2, 3], [4, 5, 6])) = }')
# 当有多个可迭代对象时，最短的可迭代对象耗尽则整个迭代就将结束。
def func(iterable1_elem, iterable2_elem, iterable3_elem):
    return iterable1_elem + iterable2_elem + iterable3_elem
print(f'{ map(func, ["a", "b", "c"], ["a", "b"], ["a"]) = }')
print(f'{ list(map(func, ["a", "b", "c"], ["a", "b"], ["a"])) = }')