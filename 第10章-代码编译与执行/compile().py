# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=- 1)
# 将 source 编译成代码或 AST 对象。代码对象可以被 exec() 或 eval() 执行。source 可以是常规的字符串、字节字符串，或者 AST 对象。参见 ast 模块的文档了解如何使用 AST 对象。
# filename 实参需要是代码读取的文件名；如果代码不需要从文件中读取，可以传入一些可辨识的值（经常会使用 '<string>'）。
# mode 实参指定了编译代码必须用的模式。如果 source 是语句序列，可以是 'exec'；如果是单一表达式，可以是 'eval'；如果是单个交互式语句，可以是 'single'。（在最后一种情况下，如果表达式执行结果不是 None 将会被打印出来。）

# 将 source 编译成代码或 AST 对象。
# source 可以是常规的字符串
# filename 可以传入一些可辨识的值（经常会使用 '<string>'）
# mode 实参指定了编译代码必须用的模式。如果 source 是语句序列，可以是 'exec'；
# 代码对象可以被 exec() 或 eval() 执行。
src = """
for i in range(3):
    print(i)
"""
print(f'{ compile(src, "<string>", "exec") = }')
exec(compile(src, "<string>", "exec"))
# mode 如果是单一表达式，可以是 'eval'；
print(f'{ compile("1+2+3", "<string>", "eval") = }')
print(f'{ eval(compile("1+2+3", "<string>", "eval")) = }')
# mode 如果是单个交互式语句，可以是 'single'。
# src = "name=input('请输入你的名字：')"
# exec(compile(src, "<string>", "single"))
# print(f'{ name = }')
# source 可以是常规的字符串、字节字符串，或者 AST 对象。
print('---------')
src = bytes("print('test')", "utf-8")
print(f'{ compile(src, "<bytes>", "exec") = }')
exec(compile(src, "<bytes>", "exec"))
print('---------')
import ast
src = ast.parse("print('abc')")
print(f'{ compile(src, "<ast>", "exec") = }')
exec(compile(src, "<ast>", "exec"))
# 将 source 编译成代码或 AST 对象。
print('----------')
src = "print(123)"
print(f'{ compile(src, "<string>", "exec", flags=ast.PyCF_ONLY_AST) = }')

#
# The optional arguments flags and dont_inherit control which compiler options should be activated and which future features should be allowed. If neither is present (or both are zero) the code is compiled with the same flags that affect the code that is calling compile(). If the flags argument is given and dont_inherit is not (or is zero) then the compiler options and the future statements specified by the flags argument are used in addition to those that would be used anyway. If dont_inherit is a non-zero integer then the flags argument is it -- the flags (future features and compiler options) in the surrounding code are ignored.
#
# 编译器选项和 future 语句是由比特位来指明的。 比特位可以通过一起按位 OR 来指明多个选项。 指明特定 future 特性所需的比特位可以在 __future__ 模块的 _Feature 实例的 compiler_flag 属性中找到。 编译器旗标 可以在 ast 模块中查找带有 PyCF_ 前缀的名称。
#
# optimize 实参指定编译器的优化级别；默认值 -1 选择与解释器的 -O 选项相同的优化级别。显式级别为 0 （没有优化；__debug__ 为真）、1 （断言被删除， __debug__ 为假）或 2 （文档字符串也被删除）。
#
# 如果编译的源码不合法，此函数会触发 SyntaxError 异常；如果源码包含 null 字节，则会触发 ValueError 异常。
#
# 如果您想分析 Python 代码的 AST 表示，请参阅 ast.parse()。
#
# 引发一个 审计事件 compile 附带参数 source, filename。
#
# 注解 在 'single' 或 'eval' 模式编译多行代码字符串时，输入必须以至少一个换行符结尾。 这使 code 模块更容易检测语句的完整性。
# 警告 在将足够大或者足够复杂的字符串编译成 AST 对象时，Python 解释器有可能因为 Python AST 编译器的栈深度限制而崩溃。
# 在 3.2 版更改: 允许使用 Windows 和 Mac 的换行符。在 'exec' 模式不再需要以换行符结尾。增加了 optimize 形参。
#
# 在 3.5 版更改: 之前 source 中包含 null 字节的话会触发 TypeError 异常。
#
# 3.8 新版功能: ast.PyCF_ALLOW_TOP_LEVEL_AWAIT 现在可在旗标中传入以启用对最高层级 await, async for 和 async with 的支持