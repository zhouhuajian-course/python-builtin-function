# sum(iterable, /, start=0)


# 从 start 开始自左向右对 iterable 的项求和并返回总计值。 iterable 的项通常为数字，而 start 值则不允许为字符串。

# 从 start 开始自左向右对 iterable 的项求和并返回总计值。
print(f'{ sum([1, 2, 3]) = }')
print(f'{ sum([1, 2, 3], 10) = }')
print(f'{ sum([1, 2, 3], 100) = }')
print(f'{ sum([1, 2, 3], start=100) = }')
#
# 注意点：iterable只能是位置参数，不能是关键字参数
# print(f'{ sum(iterable=[1, 2, 3], start=0) = }')
# iterable 的项通常为数字，而 start 值则不允许为字符串。
# print(f'{ sum([1, 2, 3], start="100") = }')

# 对某些用例来说，存在 sum() 的更好替代。 拼接字符串序列的更好更快方式是调用 ''.join(sequence)。 要以扩展精度对浮点值求和，请参阅 math.fsum()。 要拼接一系列可迭代对象，请考虑使用 itertools.chain()。
#
# 在 3.8 版更改: start 形参可用关键字参数形式来指定。

# 拼接字符串序列的更好更快方式是调用 ''.join(sequence)。
print(f'{ "a" + "b" + "c" = }')
# print(f'{ sum(["a", "b", "c"]) = }')
print(f'{ "".join(["a", "b", "c"]) = }')