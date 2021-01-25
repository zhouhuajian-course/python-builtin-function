# dir([object])
# 如果没有实参，则返回当前本地作用域中的名称列表。如果有实参，它会尝试返回该对象的有效属性列表。

# 如果没有实参，则返回当前本地作用域中的名称列表。
print(f'{ dir() = }')
# 如果有实参，它会尝试返回该对象的有效属性列表。
class C:
    a = 0
    def f(self):
        pass
print(f'{ dir(C) = }')
#
# 如果对象有一个名为 __dir__() 的方法，那么该方法将被调用，并且必须返回一个属性列表。这允许实现自定义 __getattr__() 或 __getattribute__() 函数的对象能够自定义 dir() 来报告它们的属性。

# 如果对象有一个名为 __dir__() 的方法，那么该方法将被调用，并且必须返回一个属性列表。这允许实现自定义 __getattr__() 或 __getattribute__() 函数的对象能够自定义 dir() 来报告它们的属性。
class C:
    def __getattribute__(self, name):
        if name == 'a1':
            return 'value1'
        else:
            raise AttributeError()
    def __getattr__(self, name):
        if name == 'a2':
            return 'value2'
    def __dir__(self):
        return ['a1', 'a2']
c = C()
print('---------')
print(f'{ c.a1 = }')
print(f'{ c.a2 = }')
print(f'{ dir(c) = }')

#
# 如果对象不提供 __dir__()，这个函数会尝试从对象已定义的 __dict__ 属性和类型对象收集信息。结果列表并不总是完整的，如果对象有自定义 __getattr__()，那结果可能不准确。
#
# 默认的 dir() 机制对不同类型的对象行为不同，它会试图返回最相关而不是最全的信息：
# 如果对象是模块对象，则列表包含模块的属性名称。
import module_test
print(f'{ dir(module_test) = }')
#
# 如果对象是类型或类对象，则列表包含它们的属性名称，并且递归查找所有基类的属性。
class A:
    a1 = 0
class B(A):
    b1 = 0
print(f'{ dir(B) = }')
# 否则，列表包含对象的属性名称，它的类属性名称，并且递归查找它的类的所有基类的属性。
class A:
    a1 = 0
class B(A):
    b1 = 0
    def __init__(self):
        self.t1 = 0
print('-------------------')
print(f'{ dir(B) = }')
print(f'{ dir(B()) = }')
#
# 返回的列表按字母表排序。例如：
print('-------------------')
print(f'{ dir(module_test) = }')
#
# >>>
# import struct
# dir()   # show the names in the module namespace
# ['__builtins__', '__name__', 'struct']
# dir(struct)   # show the names in the struct module
# ['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
#  '__initializing__', '__loader__', '__name__', '__package__',
#  '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
#  'unpack', 'unpack_from']
# class Shape:
#     def __dir__(self):
#         return ['area', 'perimeter', 'location']
# s = Shape()
# dir(s)
# ['area', 'location', 'perimeter']
# 注解 因为 dir() 主要是为了便于在交互式时使用，所以它会试图返回人们感兴趣的名字集合，而不是试图保证结果的严格性或一致性，它具体的行为也可能在不同版本之间改变。例如，当实参是一个类时，metaclass 的属性不包含在结果列表中。