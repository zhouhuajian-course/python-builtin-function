# enumerate(iterable, start=0)
# 返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。 enumerate() 返回的迭代器的 __next__() 方法返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。
#
# >>>
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# list(enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
# 等价于:
#
# def enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1