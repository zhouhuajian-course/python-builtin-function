# format(value[, format_spec])
# 将 value 转换为 format_spec 控制的“格式化”表示。format_spec 的解释取决于 value 实参的类型，但是大多数内置类型使用标准格式化语法：格式规格迷你语言。
print(f'{ format("test", "<10") = }')
print(f'{ format("test", "^10") = }')
print(f'{ format("test", ">10") = }')
print('--------')
print(f'{ format(10, "b") = }')
print(f'{ format(10, "o") = }')
print(f'{ format(10, "d") = }')
print(f'{ format(10, "x") = }')
print('--------')
print(f'{ format(10, "#x") = }')
print(f'{ format(10, "#X") = }')
print('-------------')
print(f'{ format(1, "0>4") = }')
print(f'{ format(12, "0>4") = }')
print(f'{ format(123, "0>4") = }')
print(f'{ format(1234, "0>4") = }')
print('----------')
print(f'{ format(3.1415926, ".2f") = }')
print(f'{ format(0.967, ".2%") = }')
#
# 默认的 format_spec 是一个空字符串，它通常和调用 str(value) 的结果相同。
#
# 调用 format(value, format_spec) 会转换成 type(value).__format__(value, format_spec) ，所以实例字典中的 __format__() 方法将不会调用。如果搜索到 object 有这个方法但 format_spec 不为空，format_spec 或返回值不是字符串，会触发 TypeError 异常。
#
# 在 3.4 版更改: 当 format_spec 不是空字符串时， object().__format__(format_spec) 会触发 TypeError

