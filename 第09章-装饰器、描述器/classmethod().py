# @classmethod
# 把一个方法封装成类方法。
# 一个类方法把类自己作为第一个实参，就像一个实例方法把实例自己作为第一个实参。请用以下习惯来声明类方法:
# class C:
#     @classmethod
#     def f(cls, arg1, arg2, ...): ...
# @classmethod 这样的形式称为函数的 decorator -- 详情参阅 函数定义。
class C:
    @classmethod
    def f(*args):
        print(f'{ args = }')
print(f'{ C.f = }')
C.f()

# 类方法的调用可以在类上进行 (例如 C.f()) 也可以在实例上进行 (例如 C().f())。 其所属类以外的类实例会被忽略。 如果类方法在其所属类的派生类上调用，则该派生类对象会被作为隐含的第一个参数被传入。
#
# 类方法的调用可以在类上进行 (例如 C.f()) 也可以在实例上进行 (例如 C().f())。 其所属类以外的类实例会被忽略。
class C:
    @classmethod
    def f(*args):
        print(f'{ args = }')
print('-'*20)
C.f()
C().f()
# 如果类方法在其所属类的派生类上调用，则该派生类对象会被作为隐含的第一个参数被传入。
class D(C):
    pass
print('-'*20)
D.f()

# 类方法与 C++ 或 Java 中的静态方法不同。 如果你需要后者，请参阅本节中的 staticmethod()。 有关类方法的更多信息，请参阅 标准类型层级结构。
#
# 注意点：@classmethod是一个装饰器，Python的装饰器可以像常规函数一样调用，所以classmethod可以像常规函数一样调用
class C:
    # @classmethod
    def f(*args):
        print(f'{ args = }')
    f = classmethod(f)
print('-'*20)
C.f()

# 在 3.9 版更改: 类方法现在可以包装其他 描述器 例如 property()。

# 在 3.9 版更改: 类方法现在可以包装其他 描述器 例如 property()。
# 这句话有个隐含的信息，classmethod()是一个描述器
# Python规定任何定义了__get__ __set__ __delete__特殊方法的类为描述器类，描述器类的实例是描述器
class C:
    def f(*args):
        print(f'{ args = }')
    f = classmethod(f)
print('-'*20)
print(f'{ C.f = }')
print(f'{ C.__dict__["f"] = }')
print(f'{ C.__dict__["f"].__get__(None, C) = }')
print(f'{ C.__dict__["f"].__get__(None, C) == C.f = }')

# class classmethod(object):
#     """
#     classmethod(function) -> method
#
#     Convert a function to be a class method.
#
#     A class method receives the class as implicit first argument,
#     just like an instance method receives the instance.
#     To declare a class method, use this idiom:
#
#       class C:
#           @classmethod
#           def f(cls, arg1, arg2, ...):
#               ...
#
#     It can be called either on the class (e.g. C.f()) or on an instance
#     (e.g. C().f()).  The instance is ignored except for its class.
#     If a class method is called for a derived class, the derived class
#     object is passed as the implied first argument.
#
#     Class methods are different than C++ or Java static methods.
#     If you want those, see the staticmethod builtin.
#     """
#
#     def __get__(self, *args, **kwargs):  # real signature unknown
#         """ Return an attribute of instance, which is of type owner. """
#         pass
#
#     def __init__(self, function):  # real signature unknown; restored from __doc__
#         pass
#
#     @staticmethod  # known case of __new__
#     def __new__(*args, **kwargs):  # real signature unknown
#         """ Create and return a new object.  See help(type) for accurate signature. """
#         pass
#
#     __func__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
#
#     __isabstractmethod__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
#
#     __dict__ = None  # (!) real value is "mappingproxy({'__get__': <slot wrapper '__get__' of 'classmethod' objects>, '__init__': <slot wrapper '__init__' of 'classmethod' objects>, '__new__': <built-in method __new__ of type object at 0x00007FFC49447990>, '__func__': <member '__func__' of 'classmethod' objects>, '__isabstractmethod__': <attribute '__isabstractmethod__' of 'classmethod' objects>, '__dict__': <attribute '__dict__' of 'classmethod' objects>, '__doc__': 'classmethod(function) -> method\\n\\nConvert a function to be a class method.\\n\\nA class method receives the class as implicit first argument,\\njust like an instance method receives the instance.\\nTo declare a class method, use this idiom:\\n\\n  class C:\\n      @classmethod\\n      def f(cls, arg1, arg2, ...):\\n          ...\\n\\nIt can be called either on the class (e.g. C.f()) or on an instance\\n(e.g. C().f()).  The instance is ignored except for its class.\\nIf a class method is called for a derived class, the derived class\\nobject is passed as the implied first argument.\\n\\nClass methods are different than C++ or Java static methods.\\nIf you want those, see the staticmethod builtin.'})"
#
