# setattr(object, name, value)
# 此函数与 getattr() 两相对应。 其参数为一个对象、一个字符串和一个任意值。 字符串指定一个现有属性或者新增属性。 函数会将值赋给该属性，只要对象允许这种操作。 例如，setattr(x, 'foobar', 123) 等价于 x.foobar = 123。

# 字符串指定一个现有属性或者新增属性。 函数会将值赋给该属性，只要对象允许这种操作。
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
cat = Cat('Lucy', 3)
print(f'{ cat.name = }')
print(f'{ cat.age = }')
setattr(cat, 'age', 6)
print(f'{ cat.age = }')
setattr(cat, 'education', 'Harvard University')
print(f'{ cat.education = }')
cat.education = 'MIT'
print(f'{ cat.education = }')

# 注意点：要设置实例方法，需要设置类属性，而不是实例属性，设置实例属性会变成普通函数
def intro(self):
    return f"小猫的名字叫{self.name}，今年{self.age}岁。"
# setattr(cat, 'intro', intro)
setattr(Cat, 'intro', intro)
print(f'{ cat.intro = }')
print(f'{ cat.intro() = }')
