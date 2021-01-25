# @staticmethod
# 将方法转换为静态方法。
#
# 静态方法不会接收隐式的第一个参数。要声明一个静态方法，请使用此语法
#
# class C:
#     @staticmethod
#     def f(arg1, arg2, ...): ...
# @staticmethod 这样的形式称为函数的 decorator -- 详情参阅 函数定义。
class C:
    @staticmethod
    def f(*args):
        print(f'{ args = }')
C.f()
C().f()
# 静态方法的调用可以在类上进行 (例如 C.f()) 也可以在实例上进行 (例如 C().f())。
#
# Python中的静态方法与Java或C ++中的静态方法类似。另请参阅 classmethod() ，用于创建备用类构造函数的变体。
#
# 像所有装饰器一样，也可以像常规函数一样调用 staticmethod ，并对其结果执行某些操作。比如某些情况下需要从类主体引用函数并且您希望避免自动转换为实例方法。对于这些情况，请使用此语法:
#
# class C:
#     builtin_open = staticmethod(open)
# 想了解更多有关静态方法的信息，请参阅 标准类型层级结构 。

# 像所有装饰器一样，也可以像常规函数一样调用 staticmethod ，并对其结果执行某些操作。比如某些情况下需要从类主体引用函数并且您希望避免自动转换为实例方法。
class C:
    # @staticmethod
    def f(*args):
        print(f'{ args = }')
    f = staticmethod(f)
    builtin_abs = staticmethod(abs)
print('-'*20)
C.f()
print(f'{ C.builtin_abs(-5) = }')