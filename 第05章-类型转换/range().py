# class range(stop)
# class range(start, stop[, step])
# 等差数列
# range 构造器的参数必须为整数（可以是内置的 int 或任何实现了 __index__ 特殊方法的对象）。 如果省略 step 参数，其默认值为 1。 如果省略 start 参数，其默认值为 0，如果 step 为零则会引发 ValueError。
print(f'{ range(3) = }')
print(f'{ list(range(3)) = }')
print(f'{ list(range(0, 3)) = }')
print(f'{ list(range(0, 3, 1)) = }')
# print(f'{ list(range(0, 3, 0)) = }')
#
# 如果 step 为正值，确定 range r 内容的公式为 r[i] = start + step*i 其中 i >= 0 且 r[i] < stop。
print('-----------')
print(f'{ list(range(0, 2, 1)) = }')
# 如果 step 为负值，确定 range 内容的公式仍然为 r[i] = start + step*i，但限制条件改为 i >= 0 且 r[i] > stop.
print('-----------')
print(f'{ list(range(0, -2, -1)) = }')
# 如果 r[0] 不符合值的限制条件，则该 range 对象为空。 range 对象确实支持负索引，但是会将其解读为从正索引所确定的序列的末尾开始索引。
print('-----------')
print(f'{ list(range(0, -2, 1)) = }')
print(f'{ list(range(0)) = }')
# 元素绝对值大于 sys.maxsize 的 range 对象是被允许的，但某些特性 (例如 len()) 可能引发 OverflowError。
#
# 一些 range 对象的例子:
#
# >>>
# >>> list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list(range(0, 30, 5))
# [0, 5, 10, 15, 20, 25]
# >>> list(range(0, 10, 3))
# [0, 3, 6, 9]
# >>> list(range(0, -10, -1))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# >>> list(range(0))
# []
# >>> list(range(1, 0))
# []