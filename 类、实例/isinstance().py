# isinstance(object, classinfo)
# 如果参数 object 是参数 classinfo 的实例或者是其 (直接、间接或 虚拟) 子类则返回 True。 如果 object 不是给定类型的对象，函数将总是返回 False。 如果 classinfo 是类型对象元组（或由其他此类元组递归组成的元组），那么如果 object 是其中任何一个类型的实例就返回 True。 如果 classinfo 既不是类型，也不是类型元组或类型元组的元组，则将引发 TypeError 异常

# 如果参数 object 是参数 classinfo 的实例或者是其 (直接、间接或 虚拟) 子类则返回 True。
print(f'{ isinstance(True, bool) = }')
print(f'{ isinstance(123, int) = }')
print(f'{ isinstance("test", str) = }')
print('----')
class A:
    pass
class B(A):
    pass
class C(B):
    pass
c = C()
print(f'{ isinstance(c, C) = }')
print(f'{ isinstance(c, B) = }')
print(f'{ isinstance(c, A) = }')
#  如果 object 不是给定类型的对象，函数将总是返回 False。
print('------')
print(f'{ isinstance(123, str) = }')
print(f'{ isinstance("test", bool) = }')
#  如果 classinfo 是类型对象元组（或由其他此类元组递归组成的元组），那么如果 object 是其中任何一个类型的实例就返回 True。
print('---------')
print(f'{ isinstance("test", (bool, int)) = }')
print(f'{ isinstance("test", (bool, int, str)) = }')
print(f'{ isinstance("test", (bool, (int, float, complex), (str, (bytes, bytearray)))) = }')
#
#  如果 classinfo 既不是类型，也不是类型元组或类型元组的元组，则将引发 TypeError 异常
print('---------')
# print(f'{ isinstance("test", "test") = }')
print(f'{ isinstance("test", [bool, int, str]) = }')
