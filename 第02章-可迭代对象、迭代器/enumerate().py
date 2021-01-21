# enumerate(iterable, start=0)
# 枚举
# enumerate
# 返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。 enumerate() 返回的迭代器的 __next__() 方法返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。
#
# 返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。
print(f'{ enumerate("abc") = }')
print(f'{ enumerate(iter("abc")) = }')
print(f'{ enumerate(["a", "b", "c"]) = }')
#  enumerate() 返回的迭代器的 __next__() 方法返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。
print('--------------')
iterable = ["a", "b", "c"]
enum = enumerate(iterable, start=0)
print(f'{ enum = }')
print(f'{ enum.__next__() = }')
print(f'{ enum.__next__() = }')
print(f'{ enum.__next__() = }')
print('------------')
print(f'{ list(enumerate(["a", "b", "c"], start=0)) = }')
print(f'{ list(enumerate(["a", "b", "c"], start=3)) = }')
print(f'{ list(enumerate(["a", "b", "c"], start=100)) = }')
print('--------------')
students = ['小明', '小红', '小灰']
# 需求：输出第几个学生是某某某
i = 0
for student in students:
    print(f'第{i+1}个学生是{student}')
    i += 1
print('--------------')
for i, student in enumerate(students, start=0):
    print(f'第{i+1}个学生是{student}')
print('--------------')
for i, student in enumerate(students, start=1):
    print(f'第{i}个学生是{student}')
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