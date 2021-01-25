# breakpoint(*args, **kws)
# 此函数会在调用时将你陷入调试器中。具体来说，它调用 sys.breakpointhook() ，直接传递 args 和 kws 。默认情况下， sys.breakpointhook() 调用 pdb.set_trace() 且没有参数。在这种情况下，它纯粹是一个便利函数，因此您不必显式导入 pdb 且键入尽可能少的代码即可进入调试器。但是， sys.breakpointhook() 可以设置为其他一些函数并被 breakpoint() 自动调用，以允许进入你想用的调试器。
#
# 引发一个 审计事件 builtins.breakpoint 并附带参数 breakpointhook。
#
# 3.7 新版功能.

# 此函数会在调用时将你陷入调试器中。
var = 123
def func():
    print("调用了func函数")
class C():
    def __init__(self):
        print("生成了C类实例")
print("输出变量 var 的值", var)
# breakpoint()  # 断点的意思
# 具体来说，它调用 sys.breakpointhook() ，直接传递 args 和 kws 。默认情况下， sys.breakpointhook() 调用 pdb.set_trace() 且没有参数。在这种情况下，它纯粹是一个便利函数，因此您不必显式导入 pdb 且键入尽可能少的代码即可进入调试器。
# 调用breakpoint()等价于
# import sys
# sys.breakpointhook()
# 等价于
# import pdb
# pdb.set_trace()
# 但是， sys.breakpointhook() 可以设置为其他一些函数并被 breakpoint() 自动调用，以允许进入你想用的调试器。
# 默认调试器是pdb.set_trace()
# PYTHONBREAKPOINT
import os
# print(os.environ) # 当前进程的环境变量
os.environ['PYTHONBREAKPOINT'] = 'debugger.another_debugger'
breakpoint(1, 2, arg3=3, arg4=4)
func()
c = C()
