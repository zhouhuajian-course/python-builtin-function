# class type(object)
# class type(name, bases, dict)
# 传入一个参数时，返回 object 的类型。 返回值是一个 type 对象，通常与 object.__class__ 所返回的对象相同。

# 传入一个参数时，返回 object 的类型。 返回值是一个 type 对象，通常与 object.__class__ 所返回的对象相同。
print(f'{ type("test") = }')
print(f'{ type(type("test")) = }')
print(f'{ "test".__class__ = }')
print(f'{ "test".__class__ == type("test") = }')
#
# 推荐使用 isinstance() 内置函数来检测对象的类型，因为它会考虑子类的情况。
#
# 传入三个参数时，返回一个新的 type 对象。 这在本质上是 class 语句的一种动态形式。 name 字符串即类名并且会成为 __name__ 属性；bases 元组列出基类并且会成为 __bases__ 属性；而 dict 字典为包含类主体定义的命名空间并且会被复制到一个标准字典成为 __dict__ 属性。
class Animal: pass
class Pet: pass
# class Cat(Animal, Pet):
#     name = "小猫"
#     age = 0
#     def get_info(self):
#         return f'小猫名字叫{self.name}，今年{self.age}岁。'
def get_info(self):
    info = f'小猫名字叫{self.name}，今年{self.age}岁。'
    return info
Cat = type('Cat',
     (Animal, Pet),
     # dict(name="小猫", age=0, get_info=lambda self: f'小猫名字叫{self.name}，今年{self.age}岁。')
     dict(name="小猫", age=0, get_info=get_info)
)
print('-----')
cat = Cat()
print(f'{ Cat.__name__ = }')
print(f'{ Cat.__bases__ = }')
print(f'{ Cat.__dict__ = }')
# print(f'{ cat.name = }')
# print(f'{ cat.age = }')
# print(f'{ cat.get_info() = }')

#
#
# 例如，下面两条语句会创建相同的 type 对象:
#
# >>>
# class X:
#     a = 1
#
# X = type('X', (object,), dict(a=1))
# 另请参阅 类型对象。
#
# 在 3.6 版更改: type 的子类如果未重载 type.__new__，将不再能使用一个参数的形式来获取对象的类型。