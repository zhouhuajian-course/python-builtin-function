"""
min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
返回可迭代对象中最小的元素，或者返回两个及以上实参中最小的。

如果只提供了一个位置参数，它必须是 iterable，返回可迭代对象中最小的元素；如果提供了两个及以上的位置参数，则返回最小的位置参数。

有两个可选只能用关键字的实参。key 实参指定排序函数用的参数，如传给 list.sort() 的。default 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。

如果有多个最小元素，则此函数将返回第一个找到的。这和其他稳定排序工具如 sorted(iterable, key=keyfunc)[0] 和 heapq.nsmallest(1, iterable, key=keyfunc) 保持一致。

3.4 新版功能: keyword-only 实参 default 。

在 3.8 版更改: key 可以为 None。
"""
# 返回可迭代对象中最小的元素，或者返回两个及以上实参中最小的。
# 如果只提供了一个位置参数，它必须是 iterable，返回可迭代对象中最小的元素；
print(f'{ min([-1.5, 2.1, -3.5, 4.0]) = }')
# 如果提供了两个及以上的位置参数，则返回最小的位置参数。
print(f'{ min(-1.5, 2.1, -3.5, 4.0) = }')
# 有两个可选只能用关键字的实参。key 实参指定排序函数用的参数，如传给 list.sort() 的。default 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。
print(f'{ min([-1.5, 2.1, -3.5, 4.0], key=abs) = }')
# default 实参是当可迭代对象为空时返回的值。
print(f'{ min([], default=0.0) = }')
print(f'{ min([], default=None) = }')
# 如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。
# print(f'{ min([]) = }')
# 如果有多个最小元素，则此函数将返回第一个找到的。
print(f'{ min([-1.5, 2.1, -3.5, 4.0, 1.5], key=abs) = }')




