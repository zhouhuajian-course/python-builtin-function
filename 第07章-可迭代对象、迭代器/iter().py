# iter(object[, sentinel]) sentinel 哨兵
# iter
# iter(iterable) -> iterator
#     iter(callable, sentinel) -> iterator

# 根据是否存在第二个实参，第一个实参的解释是非常不同的。如果没有第二个实参，object 必须是支持迭代协议（有 __iter__() 方法）的集合对象，或必须支持序列协议（有 __getitem__() 方法，且数字参数从 0 开始）。
lis = ['a', 'b', 'c']
print(f'{ hasattr(lis, "__iter__") = }')
print(f'{ iter(lis) = }')
print(f'{ list(iter(lis)) = }')
print('-------------')
string = "abc"
print(f'{ hasattr(string, "__getitem__") = }')
print(f'{ iter(string) = }')
print(f'{ list(iter(string)) = }')

# 如果有第二个实参 sentinel，那么 object 必须是可调用的对象。这种情况下生成的迭代器，每次迭代调用它的 __next__() 方法时都会不带实参地调用 object；如果返回的结果是 sentinel 则触发 StopIteration，否则返回调用结果。
print('--------------')
i = 1
def func():
    print("调用了func函数")
    global i
    num = i
    i += 1
    return num
# print(f'{ func() = }')
# print(f'{ func() = }')
print('----------')
sentinel = 3
iterator = iter(func, sentinel)
print(f'{ iterator = }')
# print(f'{ iterator.__next__() = }')
# print(f'{ iterator.__next__() = }')
# print(f'{ iterator.__next__() = }')
print(f'{ list(iterator) = }')
# 注意点：返回的迭代器，迭代得到的元素不包括sentinel哨兵值

# 返回一个 iterator 对象。根据是否存在第二个实参，第一个实参的解释是非常不同的。如果没有第二个实参，object 必须是支持迭代协议（有 __iter__() 方法）的集合对象，或必须支持序列协议（有 __getitem__() 方法，且数字参数从 0 开始）。如果它不支持这些协议，会触发 TypeError。如果有第二个实参 sentinel，那么 object 必须是可调用的对象。这种情况下生成的迭代器，每次迭代调用它的 __next__() 方法时都会不带实参地调用 object；如果返回的结果是 sentinel 则触发 StopIteration，否则返回调用结果。
#
# 另请参阅 迭代器类型。
#
# 适合 iter() 的第二种形式的应用之一是构建块读取器。 例如，从二进制数据库文件中读取固定宽度的块，直至到达文件的末尾:
#
# from functools import partial
# with open('mydata.db', 'rb') as f:
#     for block in iter(partial(f.read, 64), b''):
#         process_block(block)