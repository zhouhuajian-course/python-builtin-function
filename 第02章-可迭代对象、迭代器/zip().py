# zip(*iterables)
# 创建一个聚合了来自每个可迭代对象中的元素的迭代器。
#
# 返回一个元组的迭代器，其中的第 i 个元组包含来自每个参数序列或可迭代对象的第 i 个元素。
print(f'{ zip([1, 2, 3], ("a", "b", "c"), range(3)) = }')
print(f'{ list(zip([1, 2, 3], ("a", "b", "c"), range(3))) = }')

#
# 当所输入可迭代对象中最短的一个被耗尽时，迭代器将停止迭代。
print(f'{ list(zip([1, 2, 3], ("a", "b", "c", "d"))) = }')
#
# 当只有一个可迭代对象参数时，它将返回一个单元组的迭代器。
print('------------')
print(f'{ list(zip("abc")) = }')
#
# 不带参数时，它将返回一个空迭代器。
print('------------')
print(f'{ list(zip()) = }')
#
# 相当于:
#
# def zip(*iterables):
#     # zip('ABCD', 'xy') --> Ax By
#     sentinel = object()
#     iterators = [iter(it) for it in iterables]
#     while iterators:
#         result = []
#         for it in iterators:
#             elem = next(it, sentinel)
#             if elem is sentinel:
#                 return
#             result.append(elem)
#         yield tuple(result)
# 函数会保证可迭代对象按从左至右的顺序被求值。 使得可以通过 zip(*[iter(s)]*n) 这样的惯用形式将一系列数据聚类为长度为 n 的分组。 这将重复 同样的 迭代器 n 次，以便每个输出的元组具有第 n 次调用该迭代器的结果。 它的作用效果就是将输入拆分为长度为 n 的数据块。
#
# 当你不用关心较长可迭代对象末尾不匹配的值时，则 zip() 只须使用长度不相等的输入即可。 如果那些值很重要，则应改用 itertools.zip_longest()。
#
# zip() 与 * 运算符相结合可以用来拆解一个列表:
#
# >>>
# >>> x = [1, 2, 3]
# >>> y = [4, 5, 6]
# >>> zipped = zip(x, y)
# >>> list(zipped)
# [(1, 4), (2, 5), (3, 6)]
# >>> x2, y2 = zip(*zip(x, y))
# >>> x == list(x2) and y == list(y2)
# True