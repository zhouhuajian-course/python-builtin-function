# class object
# 返回一个没有特征的新对象。object 是所有类的基类。它具有所有 Python 类实例的通用方法。这个函数不接受任何实参。
#
# 注解 由于 object 没有 __dict__，因此无法将任意属性赋给 object 的实例

# 返回一个没有特征的新对象。
print(f'{ object() = }')
# object 是所有类的基类。它具有所有 Python 类实例的通用方法。
print(f'{ object().__str__() = }')
print(f'{ object().__repr__() = }')
print(f'{ object().__hash__() = }')
print(f'{ object().__dir__() = }')
# 由于 object 没有 __dict__，因此无法将任意属性赋给 object 的实例
print(f'{ hasattr(object, "__dict__") = }')
print(f'{ hasattr(object(), "__dict__") = }')
x = object()
# x.test = 123
# setattr(x, 'test', 123)