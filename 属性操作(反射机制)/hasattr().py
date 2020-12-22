# hasattr(object, name)
# 该实参是一个对象和一个字符串。如果字符串是对象的属性之一的名称，则返回 True，否则返回 False。（此功能是通过调用 getattr(object, name) 看是否有 AttributeError 异常来实现的。）

# 该实参是一个对象和一个字符串。如果字符串是对象的属性之一的名称，则返回 True，否则返回 False。
class Pet:
    def __init__(self, name):
        self.name = name
    def run(self):
        return f'{self.name} is running.'
pet = Pet('Lucy')
print(f'{ pet.name = }')
print(f'{ pet.run = }')
print(f'{ pet.run() = }')
print(f'{ hasattr(pet, "name") = }')
print(f'{ hasattr(pet, "run") = }')
print(f'{ hasattr(Pet, "run") = }')

print(f'{ hasattr(pet, "age") = }')
print(f'{ hasattr(pet, "money") = }')
# （此功能是通过调用 getattr(object, name) 看是否有 AttributeError 异常来实现的。）
def hasattr_test(object, name):
    res = True
    try:
        getattr(object, name)
    except AttributeError:
        res = False
    return res
print(f'{ hasattr(pet, "name") = }')
print(f'{ hasattr(pet, "money") = }')
print(f'{ hasattr_test(pet, "name") = }')
print(f'{ hasattr_test(pet, "money") = }')