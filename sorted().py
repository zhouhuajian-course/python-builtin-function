# sorted(iterable, *, key=None, reverse=False)
# 这个内置函数有三个参数iterable，key和reverse，第二个参数*星号，表示后面两个参数key和reverse必须使用关键字参数


# 根据 iterable 中的项返回一个新的已排序列表。
# reverse默认为False，默认升序排序
print(f'{ sorted(["b", "c", "a"]) = }')
print(f'{ sorted((2, 3, 1)) = }')
print(f'{ sorted(range(3)) = }')
print(f'{ sorted("bca") = }')
# 具有两个可选参数，它们都必须指定为关键字参数。
# key 指定带有单个参数的函数，用于从 iterable 的每个元素中提取用于比较的键 (例如 key=str.lower)。 默认值为 None (直接比较元素)。
print('--------')
print(f'{ sorted(["B", "c", "a"]) = }')
print(f'{ sorted(["B", "c", "a"], key=str.lower) = }')
print(f'{ sorted(["B", "c", "a"], key=lambda elem: elem.lower()) = }')
print('--------')
student_scores = [('小红', 100), ('小明', 99), ('小黑', 86)]
print(f'{ sorted(student_scores, key=lambda elem: elem[1]) = }')
#
# reverse 为一个布尔值。 如果设为 True，则每个列表元素将按反向顺序比较进行排序。
print('---------')
print(f'{ sorted(["b", "c", "a"], reverse=True) = }')
print(f'{ sorted((2, 3, 1), reverse=True) = }')
print(f'{ sorted(range(3), reverse=True) = }')
print(f'{ sorted("bca", reverse=True) = }')
student_scores = [('小红', 100), ('小明', 99), ('小黑', 86)]
print(f'{ sorted(student_scores, key=lambda elem: elem[1], reverse=True) = }')
#
# 使用 functools.cmp_to_key() 可将老式的 cmp 函数转换为 key 函数。
#
# 内置的 sorted() 确保是稳定的。 如果一个排序确保不会改变比较结果相等的元素的相对顺序就称其为稳定的 --- 这有利于进行多重排序（例如先按部门、再按薪级排序）。
print('-----------')
student_scores = [('小红', 100), ('小明', 99), ('小黑', 86), ('小灰', 100)]
print(f'{ sorted(student_scores, key=lambda elem: elem[1], reverse=False) = }')
print(f'{ sorted(student_scores, key=lambda elem: elem[1], reverse=True) = }')
print('---------')
student_scores = {"Tom": 100, "Lucy": 80, "Jack": 100}
print(f'{ student_scores.items() = }')
print(f'{ list(student_scores.items()) = }')
print(f'{ sorted(student_scores.items(), key=lambda elem: (elem[1])) = }')
print(f'{ sorted(student_scores.items(), key=lambda elem: (elem[1], elem[0])) = }')
print(f'{ dict(sorted(student_scores.items(), key=lambda elem: (elem[1], elem[0]))) = }')
# {'Lucy': 80, 'Jack': 100, 'Tom': 100}
print('---------')
L = [(6, 6), (9, 5), (6, 10), (8, 4)]
# 第一个元素升序，如果第一个元素一样，则第二个元素降序
print(f'{ sorted([(6, 6), (9, 5), (6, 10), (8, 4)], key=lambda elem: (elem[0], -elem[1])) = }')
# 第一个元素降序，如果第一个元素一样，则第二个元素升序
print(f'{ sorted([(6, 6), (9, 5), (6, 10), (8, 4)], key=lambda elem: (-elem[0], elem[1])) = }')
# 有关排序示例和简要排序教程，请参阅 排序指南 。