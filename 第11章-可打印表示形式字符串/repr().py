# repr(object)
# return printable
# 返回包含一个对象的可打印表示形式的字符串。 对于许多类型来说，该函数会尝试返回的字符串将会与该对象被传递给 eval() 时所生成的对象具有相同的值，在其他情况下表示形式会是一个括在尖括号中的字符串，其中包含对象类型的名称与通常包括对象名称和地址的附加信息。 类可以通过定义 __repr__() 方法来控制此函数为它的实例所返回的内容。

# 返回包含一个对象的可打印表示形式的字符串。
print(f'{ repr(123) = }')
print(f'{ str(123) = }')
print(f'{ repr(1.23) = }')
print(f'{ str(1.23) = }')
print(f'{ repr([1, 2, 3]) = }')
print(f'{ str([1, 2, 3]) = }')
print('------')
print(f'{ repr("abc") = }')
print(f'{ str("abc") = }')
print('------')
print(
    len(repr("abc")),
    len(str("abc")),
    repr("abc")[0],
    repr("a\"bc")[0],
    repr("a'bc")[0],
    repr("a'\"bc")[0],
)
print('------')
import datetime
date_test = datetime.date(year=1970, month=1, day=1)
print(f'{ repr(date_test) = }')
print(f'{ str(date_test) = }')
# 对于许多类型来说，该函数会尝试返回的字符串将会与该对象被传递给 eval() 时所生成的对象具有相同的值
print('-------')
print(f'{ eval(repr(123)) = }')
print(f'{ eval(repr(123)) == 123 = }')
print(f'{ eval(repr("test")) = }')
print(f'{ eval(repr("test")) == "test" = }')
print(f'{ eval(repr([1, 2, 3])) = }')
print(f'{ eval(repr([1, 2, 3])) == [1, 2, 3] = }')
print('------')
date_test = datetime.date(year=1970, month=1, day=1)
print(f'{ repr(date_test) = }')
print(f'{ eval(repr(date_test)) == date_test = }')
# 在其他情况下表示形式会是一个括在尖括号中的字符串，其中包含对象类型的名称与通常包括对象名称和地址的附加信息。
class C:
    pass
print('------')
print(f'{ repr(C()) = }')
# 类可以通过定义 __repr__() 方法来控制此函数为它的实例所返回的内容。
class C:
    def __repr__(self):
        return "测试"
print('------')
print(f'{ repr(C()) = }')