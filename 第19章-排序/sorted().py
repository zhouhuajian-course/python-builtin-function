# sorted(iterable, *, key=None, reverse=False)

# 根据 iterable 中的项返回一个新的已排序列表。
# 具有两个可选参数，它们都必须指定为关键字参数。
# reverse=False reverse 次序颠倒 在这里表示，是否倒序排序，默认为False，表示默认升序排序
print(f'{ sorted(["b", "c", "a"]) = }')
print(f'{ sorted((2, 3, 1)) = }')
print(f'{ sorted("bca") = }')

#
# key 指定带有单个参数的函数，用于从 iterable 的每个元素中提取用于比较的键 (例如 key=str.lower)。 默认值为 None (直接比较元素)。
print('---------')
student_scores = [('小明', 99), ('小红', 100), ('小灰', 86)]
def get_comparison_key(elem):
    return elem[1]
print(f'{ sorted(student_scores, key=get_comparison_key) = }')
print(f'{ sorted(student_scores, key=lambda elem: elem[1]) = }')
#
# reverse 为一个布尔值。 如果设为 True，则每个列表元素将按反向顺序比较进行排序。
print('----------')
print(f'{ sorted((2, 3, 1)) = }')
print(f'{ sorted((2, 3, 1), reverse=True) = }')
print(f'{ sorted(student_scores, key=lambda elem: elem[1]) = }')
print(f'{ sorted(student_scores, key=lambda elem: elem[1], reverse=True) = }')
# 使用 functools.cmp_to_key() 可将老式的 cmp 函数转换为 key 函数。
#
# 内置的 sorted() 确保是稳定的。 如果一个排序确保不会改变比较结果相等的元素的相对顺序就称其为稳定的 --- 这有利于进行多重排序（例如先按部门、再按薪级排序）。
print('--------')
student_scores = [('小明', 99), ('小红', 99), ('小灰', 86)]
print(f'{ sorted(student_scores, key=lambda elem: elem[1]) = }')
print('---------')
# 需求 按分数正排序，如果分数一样，按身高正排序
students = [('小明', 99, 170), ('小红', 99, 165), ('小灰', 86, 180)]
# 用于比较的键是(99, 170) (99, 165) (86, 180)
print(f'{ sorted(students, key=lambda elem: (elem[1], elem[2])) = }')
#
# 有关排序示例和简要排序教程，请参阅 排序指南 。
