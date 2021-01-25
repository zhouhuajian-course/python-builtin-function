# exec(object[, globals[, locals]])
# # 这个函数支持动态执行 Python 代码。object 必须是字符串或者代码对象。如果是字符串，那么该字符串将被解析为一系列 Python 语句并执行（除非发生语法错误）。
exec("for i in range(3): print(i)")
# 如果是代码对象，它将被直接执行。
print('-----------')
print(f'{ compile("for i in range(3): print(i)", "<string>", "exec") = }')
print('-----------')
exec(compile("for i in range(3): print(i)", "<string>", "exec"))

# 这个函数支持动态执行 Python 代码。object 必须是字符串或者代码对象。如果是字符串，那么该字符串将被解析为一系列 Python 语句并执行（除非发生语法错误）。1 如果是代码对象，它将被直接执行。在任何情况下，被执行的代码都需要和文件输入一样是有效的（见参考手册中关于文件输入的章节）。请注意即使在传递给 exec() 函数的代码的上下文中，return 和 yield 语句也不能在函数定义之外使用。该函数返回值是 None 。
#
# 无论哪种情况，如果省略了可选项，代码将在当前作用域内执行。 如果只提供了 globals，则它必须是一个字典（不能是字典的子类），该字典将同时被用于全局和局部变量。 如果同时提供了 globals 和 locals，它们会分别被用于全局和局部变量。 如果提供了 locals，则它可以是任何映射对象。 请记住在模块层级上，globals 和 locals 是同一个字典。 如果 exec 得到两个单独对象作为 globals 和 locals，则代码将如同嵌入类定义的情况一样执行。

# # 无论哪种情况，如果省略了可选项，代码将在当前作用域内执行。 如果只提供了 globals，则它必须是一个字典（不能是字典的子类），该字典将同时被用于全局和局部变量。
a = 2
b = 3
print('---------')
exec("print(a*b)")
print('---------')
exec("print(a*b)", dict(a=5, b=6))
# 注意点：代码有语法错误，会报语法错误异常
exec("print(a++)")
#
# 如果 globals 字典不包含 __builtins__ 键值，则将为该键插入对内建 builtins 模块字典的引用。因此，在将执行的代码传递给 exec() 之前，可以通过将自己的 __builtins__ 字典插入到 globals 中来控制可以使用哪些内置代码。
#
# 引发一个 审计事件 exec 附带参数 code_object。
#
# 注解 内置 globals() 和 locals() 函数各自返回当前的全局和本地字典，因此可以将它们传递给 exec() 的第二个和第三个实参。
# 注解 默认情况下，locals 的行为如下面 locals() 函数描述的一样：不要试图改变默认的 locals 字典。如果您想在 exec() 函数返回时知道代码对 locals 的变动，请明确地传递 locals 字典。