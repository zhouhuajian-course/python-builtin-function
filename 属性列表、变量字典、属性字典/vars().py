# vars([object])
# 返回模块、类、实例或任何其它具有 __dict__ 属性的对象的 __dict__ 属性。
#
# 返回模块、类、实例或任何其它具有 __dict__ 属性的对象的 __dict__ 属性。
import module_test
print(f'{ module_test.__dict__ = }')
print('-------------------------------')
print(f'{ vars(module_test) = }')
print('-------------------------------')
print(f'{ vars(module_test) == module_test.__dict__ = }')

class C:
    a1 = 0
    def __init__(self):
        self.t1 = 0
    def m1(self):
        pass
print('-------------------------------')
print(f'{ C.__dict__ = }')
print('-------------------------------')
print(f'{ vars(C) = }')
print('-------------------------------')
print(f'{ vars(C) == C.__dict__ = }')

print('-------------------------------')
c = C()
print(f'{c.__dict__ = }')
print('-------------------------------')
print(f'{ vars(c) = }')
print('-------------------------------')
print(f'{ vars(c) == c.__dict__ = }')
# 模块和实例这样的对象具有可更新的 __dict__ 属性；但是，其它对象的 __dict__ 属性可能会设为限制写入（例如，类会使用 types.MappingProxyType 来防止直接更新字典）。
#
# 不带参数时，vars() 的行为类似 locals()。 请注意，locals 字典仅对于读取起作用，因为对 locals 字典的更新会被忽略。

# 不带参数时，vars() 的行为类似 locals()。
def f(a, b):
    v = 0
    def f_test(): pass
    class C: pass
    print(f'{ vars() = }')
    print(f'{ locals() = }')
    print(f'{ vars() == locals() = }')
print('-------')
f(1, 2)
#
# 如果指定了一个对象但它没有 __dict__ 属性（例如，当它所属的类定义了 __slots__ 属性时）则会引发 TypeError 异常。

# 如果指定了一个对象但它没有 __dict__ 属性（例如，当它所属的类定义了 __slots__ 属性时）则会引发 TypeError 异常。
class C:
    __slots__ = ('a1', 'a2', 'a3')
    pass
print('-------')
c = C()
print(f'{ hasattr(c, "__dict__") = }')
print(f'{ vars(c) = }')

# module_test
# v1 = 0
# def f1(): pass
# class C1(): pass