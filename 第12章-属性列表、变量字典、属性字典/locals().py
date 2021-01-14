# locals()
# 更新并返回表示当前本地符号表的字典。 在函数代码块但不是类代码块中调用 locals() 时将返回自由变量。 请注意在模块层级上，locals() 和 globals() 是同一个字典。
#
# 注解 不要更改此字典的内容；更改不会影响解释器使用的局部变量或自由变量的值。

# 更新并返回表示当前本地符号表的字典。 在函数代码块但不是类代码块中调用 locals() 时将返回自由变量。
def f(arg):
    v = 0
    def f_test():
        pass
    class C():
        pass
    print(f'{ locals() = }')
f(1)
# 请注意在模块层级上，locals() 和 globals() 是同一个字典。
print('--------')
print(f'{ locals() == globals() = }')
# 注解 不要更改此字典的内容；更改不会影响解释器使用的局部变量或自由变量的值。
def f(arg):
    v = 0
    def f_test():
        pass
    class C():
        pass
    locals()['v'] = 3
    print(f'{ v = }')
    print(f'{ locals() = }')
print('------------')
f(1)