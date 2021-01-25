# issubclass(class, classinfo)
# 如果 class 是 classinfo 的 (直接、间接或 虚拟) 子类则返回 True。 类会被视作其自身的子类。 classinfo 也以是类对象的元组，在此情况下 classinfo 中的每个条目都将被检查。 在任何其他情况下，都将引发 TypeError 异常。

# 如果 class 是 classinfo 的 (直接、间接或 虚拟) 子类则返回 True。
class A:
    pass
class B(A):
    pass
class C(B):
    pass
print(f'{ issubclass(B, A) = }')
print(f'{ issubclass(C, B) = }')
print(f'{ issubclass(C, A) = }')
print(f'{ issubclass(C, int) = }')
# 类会被视作其自身的子类。
print('---')
print(f'{ issubclass(A, A) = }')
# classinfo 也以是类对象的元组，在此情况下 classinfo 中的每个条目都将被检查。
print('-----')
print(f'{ issubclass(B, (int, str)) = }')
print(f'{ issubclass(B, (int, str, A)) = }')
print(f'{ issubclass(B, (int, str, (float, A))) = }')
# 在任何其他情况下，都将引发 TypeError 异常。
print('-----------')
# print(f'{ issubclass(B, 123) = }')
# print(f'{ issubclass(B, [int, str, A]) = }')