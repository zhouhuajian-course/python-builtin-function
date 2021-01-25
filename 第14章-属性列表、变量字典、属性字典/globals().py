# globals()
# 返回表示当前全局符号表的字典。这总是当前模块的字典（在函数或方法中，不是调用它的模块，而是定义它的模块）。

# 返回表示当前全局符号表的字典。
import sys
v = 0
def f(): pass
class C(): pass
print(f'{ globals() = }')
# 这总是当前模块的字典（在函数或方法中，不是调用它的模块，而是定义它的模块）。
import module_test
print('----------------------')
module_test.f1()
print('----------------------')
module_test.C1().m1()

# module test
# v1 = 0
# def f1():
#     print(f'{ globals() = }')
# class C1():
#     def m1(self):
#         print(f'{ globals() = }')