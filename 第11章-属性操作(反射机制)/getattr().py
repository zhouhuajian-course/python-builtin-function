# getattr(object, name[, default])
# 返回对象命名属性的值。name 必须是字符串。如果该字符串是对象的属性之一，则返回该属性的值。例如， getattr(x, 'foobar') 等同于 x.foobar。如果指定的属性不存在，且提供了 default 值，则返回它，否则触发 AttributeError。

# 返回对象命名属性的值。name 必须是字符串。如果该字符串是对象的属性之一，则返回该属性的值。
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        return f"这只小狗叫{self.name}，年龄{self.age}岁。"
dog = Dog('小念', 2)
print(f'{ getattr(dog, "name") = }')
print(f'{ getattr(dog, "age") = }')
print(f'{ getattr(dog, "intro") = }')
print(f'{ getattr(dog, "intro")() = }')
# 如果指定的属性不存在，且提供了 default 值，则返回它，否则触发 AttributeError。
# print(f'{ getattr(dog, "run") = }')
# print(f'{ getattr(dog, "run", None) = }')
# print(f'{ getattr(dog, "education") = }')
print(f'{ getattr(dog, "education", "unknown") = }')