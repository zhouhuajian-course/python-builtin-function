# super([type[, object-or-type]])
# super
# super() -> same as super(__class__, <first argument>)
#     super(type) -> unbound super object
#     super(type, obj) -> bound super object; requires isinstance(obj, type)
#     super(type, type2) -> bound super object; requires issubclass(type2, type)
class B:
    def test(self):
        print("B test")
class C(B):
    def test(self):
        print("C test")
        # super().test()
        super(C, self).test() # MRO 方法解析顺序
        # self mro  C->B->object
C().test()
print('------')
print(f'{ super(C) = }') # unbound super object
print('-------')
class B:
    @classmethod
    def test(cls):
        print("B test")
class C(B):
    @classmethod
    def test(cls):
        print("C test")
        # super().test()
        # print(f'{ cls = }')
        # super(type, type2) -> bound super object
        super(C, C).test()
C.test()
# 它会将方法调用委托给 type 或兄弟类
class A:
    def test(self):
        print("A test")
class B(A):
    def test(self):
        print("B test")
        print(f'{ self = }')
        print(f'{ type(self).mro() = }')
        super(B, self).test()
        # self 是D类的实例 mro D->B->C->A->object
        # C类是B的兄弟类，而不是父类
class C(A):
    def test(self):
        print("C test")
class D(B, C):
    def test(self):
        print("D test")
        super(D, self).test()
print('-------')
D().test()
# 返回一个代理对象，它会将方法调用委托给 type 的父类或兄弟类。 这对于访问已在类中被重载的继承方法很有用。
# object-or-type 确定用于搜索的 method resolution order。 搜索会从 type 之后的类开始。
#
# 举例来说，如果 object-or-type 的 __mro__ 为 D -> B -> C -> A -> object 并且 type 的值为 B，则 super() 将会搜索 C -> A -> object。
#
# object-or-type 的 __mro__ 属性列出了 getattr() 和 super() 所共同使用的方法解析搜索顺序。 该属性是动态的，可以在任何继承层级结构发生更新的时候被改变。
#
# 如果省略第二个参数，则返回的超类对象是未绑定的。 如果第二个参数为一个对象，则 isinstance(obj, type) 必须为真值。 如果第二个参数为一个类型，则 issubclass(type2, type) 必须为真值（这适用于类方法）。
#
# super 有两个典型用例。 在具有单继承的类层级结构中，super 可用来引用父类而不必显式地指定它们的名称，从而令代码更易维护。 这种用法与其他编程语言中 super 的用法非常相似。
#
# 第二个用例是在动态执行环境中支持协作多重继承。 此用例为 Python 所独有，在静态编译语言或仅支持单继承的语言中是不存在的。 这使得实现“菱形图”成为可能，在这时会有多个基类实现相同的方法。 好的设计强制要求这种方法在每个情况下具有相同的调用签名（因为调用顺序是在运行时确定的，也因为该顺序要适应类层级结构的更改，还因为该顺序可能包含在运行时之前未知的兄弟类）。
#
# 对于以上两个用例，典型的超类调用看起来是这样的:
#
# class C(B):
#     def method(self, arg):
#         super().method(arg)    # This does the same thing as:
#                                # super(C, self).method(arg)
# 除了方法查找之外，super() 也可用于属性查找。 一个可能的应用场合是在上级或同级类中调用 描述器。
#
# 请注意 super() 是作为显式加点属性查找的绑定过程的一部分来实现的，例如 super().__getitem__(name)。 它做到这一点是通过实现自己的 __getattribute__() 方法，这样就能以可预测的顺序搜索类，并且支持协作多重继承。 对应地，super() 在像 super()[name] 这样使用语句或操作符进行隐式查找时则未被定义。
#
# 还要注意的是，除了零个参数的形式以外，super() 并不限于在方法内部使用。 两个参数的形式明确指定参数并进行相应的引用。 零个参数的形式仅适用于类定义内部，因为编译器需要填入必要的细节以正确地检索到被定义的类，还需要让普通方法访问当前实例。
#
# 对于有关如何使用 super() 来如何设计协作类的实用建议，请参阅 使用 super() 的指南。