# hash(object)
# 返回该对象的哈希值（如果它有的话）。哈希值是整数。它们在字典查找元素时用来快速比较字典的键。相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0）。
#
# 注解 如果对象实现了自己的 __hash__() 方法，请注意，hash() 根据机器的字长来截断返回值。另请参阅 __hash__()

# 返回该对象的哈希值（如果它有的话）。哈希值是整数。
print(f'{ hash("test") = }')
print(f'{ hash("test") = }')
print(f'{ hash("test") = }')
print(f'{ hash((1, 2, 3)) = }')
print(f'{ hash(123456) = }')
# 相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0）。
print(f'{ hash(1) = }')
print(f'{ hash(1.0) = }')
print(f'{ hash(1+0j) = }')
print(f'{ hash(True) = }')