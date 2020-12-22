"""
max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
返回可迭代对象中最大的元素，或者返回两个及以上实参中最大的。

如果只提供了一个位置参数，它必须是非空 iterable，返回可迭代对象中最大的元素；如果提供了两个及以上的位置参数，则返回最大的位置参数。

有两个可选只能用关键字的实参。key 实参指定排序函数用的参数，如传给 list.sort() 的。default 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。

如果有多个最大元素，则此函数将返回第一个找到的。这和其他稳定排序工具如 sorted(iterable, key=keyfunc, reverse=True)[0] 和 heapq.nlargest(1, iterable, key=keyfunc) 保持一致。

3.4 新版功能: keyword-only 实参 default 。

在 3.8 版更改: key 可以为 None。
"""
# 返回可迭代对象中最大的元素，或者返回两个及以上实参中最大的。
# 如果只提供了一个位置参数，它必须是非空 iterable，返回可迭代对象中最大的元素；
# print(f'{ max([]) = }')
print(f'{ max([3, 9, -20, 15]) = }')
# 如果提供了两个及以上的位置参数，则返回最大的位置参数。
print(f'{ max(3, 9, -20, 15) = }')
# 有两个可选只能用关键字的实参。key 实参指定排序函数用的参数，如传给 list.sort() 的。default 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。
print(f'{ max([3, 9, -20, 15], key=abs) = }')
print(f'{ max([], default=None) = }')
# 如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。
# print(f'{ max([]) = }')
# 如果有多个最大元素，则此函数将返回第一个找到的
print(f'{ max([3, 9, -20, 15, 20], key=abs) = }')
# 注意点：key和default必须是关键字参数

