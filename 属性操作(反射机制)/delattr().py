# delattr(object, name)
# setattr() 相关的函数。实参是一个对象和一个字符串。该字符串必须是对象的某个属性。如果对象允许，该函数将删除指定的属性。例如 delattr(x, 'foobar') 等价于 del x.foobar 。

# 实参是一个对象和一个字符串。该字符串必须是对象的某个属性。如果对象允许，该函数将删除指定的属性。
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        return f'这只猫咪叫{self.name}，今年{self.age}岁'
cat = Cat('小明', 3)
# print(f'{ hasattr(cat, "name") = }')
# print(f'{ cat.name = }')
# delattr(cat, "name")
# print(f'{ hasattr(cat, "name") = }')
# print(f'{ cat.name = }')
# print(f'{ hasattr(cat, "intro") = }')
# print(f'{ cat.intro() = }')
# print(f'{ cat.__dict__ = }')
# print(f'{ Cat.__dict__ = }')
# delattr(cat, 'intro')
# delattr(Cat, 'intro')
# print(f'{ hasattr(cat, "intro") = }')
# print(f'{ cat.intro() = }')

#  delattr(x, 'foobar') 等价于 del x.foobar 。
print(f'{ hasattr(cat, "name") = }')
del cat.name
print(f'{ hasattr(cat, "name") = }')
