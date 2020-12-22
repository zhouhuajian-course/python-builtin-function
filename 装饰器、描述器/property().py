# class property(fget=None, fset=None, fdel=None, doc=None)
property
# 返回 property 属性。
# fget 是获取属性值的函数。 fset 是用于设置属性值的函数。 fdel 是用于删除属性值的函数。并且 doc 为属性对象创建文档字符串。
# 一个典型的用法是定义一个托管属性 x:
# class C:
#     def __init__(self):
#         self._x = None
#
#     def getx(self):
#         return self._x
#
#     def setx(self, value):
#         self._x = value
#
#     def delx(self):
#         del self._x
#     x = property(getx, setx, delx, "I'm the 'x' property.")
# 如果 c 是 C 的实例，c.x 将调用getter，c.x = value 将调用setter， del c.x 将调用deleter。
class C:
    def __init__(self):
        self._x = None
    def setx(self, value):
        print(f'调用了setx {  value = }')
        self._x = value
    def delx(self):
        print('调用了delx')
        del self._x
    def getx(self):
        """这是x属性的文档"""
        print('调用了getx')
        return self._x
    # 如果 c 是 C 的实例，c.x 将调用getter，c.x = value 将调用setter， del c.x 将调用deleter。
    # x = property(getx, setx, delx, "I'm the 'x' property.")
    x = property(getx, setx, delx)
c = C()
# print(f'{ c.x = }')
# c.x = 123
# del c.x
# print(f'{ C.x.__doc__ = }')
#
# 如果给出，doc 将成为该 property 属性的文档字符串。 否则该 property 将拷贝 fget 的文档字符串（如果存在）。 这令使用 property() 作为 decorator 来创建只读的特征属性可以很容易地实现:
# class Parrot:
#     def __init__(self):
#         self._voltage = 100000
#     @property
#     def voltage(self):
#         """Get the current voltage."""
#         return self._voltage
# 以上 @property 装饰器会将 voltage() 方法转化为一个具有相同名称的只读属性的 "getter"，并将 voltage 的文档字符串设置为 "Get the current voltage."
class Parrot:
    def __init__(self):
        self._voltage = 100000
    @property
    def voltage(self):
        """Get the current voltage."""
        print('调用了voltage的getter')
        return self._voltage
    # voltage = property(voltage)
parrot = Parrot()
# print(f'{ parrot.voltage = }')
# print(f'{ Parrot.voltage.__doc__ = }')
# parrot.voltage = 200000
#
# 特征属性对象具有 getter, setter 以及 deleter 方法，它们可用作装饰器来创建该特征属性的副本，并将相应的访问函数设为所装饰的函数。 这最好是用一个例子来解释:
# class C:
#     def __init__(self):
#         self._x = None
#     @property
#     def x(self):
#         """I'm the 'x' property."""
#         return self._x
#     @x.setter
#     def x(self, value):
#         self._x = value
#     @x.deleter
#     def x(self):
#         del self._x
# 上述代码与第一个例子完全等价。 注意一定要给附加函数与原始的特征属性相同的名称 (在本例中为 x。)
# 返回的特征属性对象同样具有与构造器参数相对应的属性 fget, fset 和 fdel。
# 在 3.5 版更改: 特征属性对象的文档字符串现在是可写的。
# class C:
#     def __init__(self):
#         self._x = None
#     def getx(self):
#         return self._x
#     def setx(self, value):
#         self._x = value
#     def delx(self):
#         del self._x
#     x = property(getx, setx, delx, "I'm the 'x' property.")
class C:
    def __init__(self):
        self._x = None
    @property
    def x(self):
        """I'm the 'x' property."""
        print('获取属性')
        return self._x
    # x = property(x)
    @x.setter
    def x(self, value):
        print('设置属性')
        self._x = value
    # x = x.setter(x)
    @x.deleter
    def x(self):
        print('删除属性')
        del self._x
    # x = x.deleter(x)
print('-'*20)
c = C()
# c.x
# c.x = 123
# del c.x

class C:
    def __init__(self):
        self._x = None
    # @property
    def x(self):
        """I'm the 'x' property."""
        print('获取属性')
        return self._x
    x = property(x)
    # @x.setter
    def temp_x(self, value):
        print('设置属性')
        self._x = value
    x = x.setter(temp_x)
    # @x.deleter
    def temp_x(self):
        print('删除属性')
        del self._x
    x = x.deleter(temp_x)
print('-'*20)
c = C()
c.x
c.x = 123
del c.x