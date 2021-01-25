# eval(expression[, globals[, locals]])
# evaluate 求...的值
# 实参是一个字符串，以及可选的 globals 和 locals。globals 实参必须是一个字典。locals 可以是任何映射对象。
# expression 参数会作为一个 Python 表达式（从技术上说是一个条件列表）被解析并求值，并使用 globals 和 locals 字典作为全局和局部命名空间。
# 如果两个字典同时省略，则表达式执行时会使用 eval() 被调用的环境中的 globals 和 locals。
# 返回值就是表达式的求值结果。
a = 1
b = 2
print(f'{ globals() = }')
print(f'{ eval("a+b") = }')
print('---------------')
print(f'{ eval("a+b", dict(a=5, b=6)) = }')
# 语法错误将作为异常被报告
# i = 0
# print(f'{ eval("i++") }')

# expression 参数会作为一个 Python 表达式（从技术上说是一个条件列表）被解析并求值，并使用 globals 和 locals 字典作为全局和局部命名空间。 如果 globals 字典存在且不包含以 __builtins__ 为键的值，则会在解析 expression 之前插入以此为键的对内置模块 builtins 的引用。 这意味着 expression 通常具有对标准 builtins 模块的完全访问权限且受限的环境会被传播。 如果省略 locals 字典则其默认值为 globals 字典。 如果两个字典同时省略，则表达式执行时会使用 eval() 被调用的环境中的 globals 和 locals。 请注意，eval() 并没有对外围环境下的 (非局部) 嵌套作用域 的访问权限。
#
# 返回值就是表达式的求值结果。 语法错误将作为异常被报告。 例如：
#
# >>>
# x = 1
# eval('x+1')
# 2
# 这个函数也可以用来执行任何代码对象（如 compile() 创建的）。这种情况下，参数是代码对象，而不是字符串。如果编译该对象时的 mode 实参是 'exec' 那么 eval() 返回值为 None 。

# 这个函数也可以用来执行任何代码对象（如 compile() 创建的）。这种情况下，参数是代码对象，而不是字符串。如果编译该对象时的 mode 实参是 'exec' 那么 eval() 返回值为 None 。
print('---------')
print(f'{ eval(compile("2+3", "<string>", "eval")) = }')
print(f'{ eval(compile("2+3", "<string>", "exec")) = }')
#
# 提示： exec() 函数支持动态执行语句。 globals() 和 locals() 函数各自返回当前的全局和本地字典，因此您可以将它们传递给 eval() 或 exec() 来使用。
#
# If the given source is a string, then leading and trailing spaces and tabs are stripped.
#
# 另外可以参阅 ast.literal_eval()，该函数可以安全执行仅包含文字的表达式字符串。
#
# 引发一个 审计事件 exec 附带参数 code_object。