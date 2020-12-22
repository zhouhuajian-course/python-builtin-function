# next(iterator[, default])
# 通过调用 iterator 的 __next__() 方法获取下一个元素。如果迭代器耗尽，则返回给定的 default，如果没有默认值则触发 StopIteration。
class Iterator:
    def __init__(self):
        self.items = [1, 2, 3]
    def __iter__(self):
        return self
    def __next__(self):
        print('调用了__next__')
        if not self.items:
            raise StopIteration
        return self.items.pop(0)
iterator = Iterator()
print(f'{ next(iterator) = }')
print(f'{ next(iterator) = }')
print(f'{ next(iterator) = }')
# print(f'{ next(iterator) = }')
print(f'{ next(iterator, None) = }')
print(f'{ next(iterator, None) = }')
# 除了自定义迭代器，大家也可以通过iter内置函数得到可迭代对象的迭代器
# 可以结合try语句实现遍历迭代器的所有元素
iterable = ['a', 'b', 'c']
iterator = iter(iterable)
while True:
    try:
        print(f'{ next(iterator) = }')
    except StopIteration:
        break