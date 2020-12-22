# class list([iterable])
# 可以用多种方式构建列表：
#
# 使用一对方括号来表示空列表: []
#
# 使用方括号，其中的项以逗号分隔: [a], [a, b, c]
#
# 使用列表推导式: [x for x in iterable]
#
# 使用类型的构造器: list() 或 list(iterable)
#
# 构造器将构造一个列表，其中的项与 iterable 中的项具有相同的的值与顺序。 iterable 可以是序列、支持迭代的容器或其它可迭代对象。 如果 iterable 已经是一个列表，将创建并返回其副本，类似于 iterable[:]。 例如，list('abc') 返回 ['a', 'b', 'c'] 而 list( (1, 2, 3) ) 返回 [1, 2, 3]。 如果没有给出参数，构造器将创建一个空列表 []。
#
# 构造器将构造一个列表，其中的项与 iterable 中的项具有相同的的值与顺序。 iterable 可以是序列、支持迭代的容器或其它可迭代对象。 如果 iterable 已经是一个列表，将创建并返回其副本，
print(f'{ list(["a", "b", "c"]) = }')
print(f'{ list((1, 2, 3)) = }')
print(f'{ list(range(3)) = }')
print(f'{ list("abc") = }')
print('--------')
print(f'{ list(filter(None, [0, 1, 2, 3])) = }')
def func(elem):
    return elem + 1
print(f'{ list(map(func, [0, 1, 2, 3])) = }')
# 如果没有给出参数，构造器将创建一个空列表 []。
print('-------')
print(f'{ list() = }')
# 其它许多操作也会产生列表，包括 sorted() 内置函数。