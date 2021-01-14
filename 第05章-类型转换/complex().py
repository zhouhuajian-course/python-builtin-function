# class complex([real[, imag]])
# 返回值为 real + imag*1j 的复数，或将字符串或数字转换为复数。如果第一个形参是字符串，则它被解释为一个复数，并且函数调用时必须没有第二个形参。第二个形参不能是字符串。每个实参都可以是任意的数值类型（包括复数）。如果省略了 imag，则默认值为零，构造函数会像 int 和 float 一样进行数值转换。如果两个实参都省略，则返回 0j。

# 返回值为 real + imag*1j 的复数，或将字符串或数字转换为复数。如果第一个形参是字符串，则它被解释为一个复数，并且函数调用时必须没有第二个形参。
print(f'{ complex("1+2j") = }')
# 每个实参都可以是任意的数值类型（包括复数）。
print('---------')
print(f'{ complex(1, 2) = }')
print(f'{ complex(1, -2) = }')
print(f'{ complex(1.2, 3.4) = }')
print(f'{ complex(1+2j, 1) = }')
# 如果省略了 imag，则默认值为零，构造函数会像 int 和 float 一样进行数值转换。
# 如果两个实参都省略，则返回 0j。
print('--------')
print(f'{ complex(1) = }')
print(f'{ complex(1.23) = }')
print(f'{ complex() = }')
#
# 对于一个普通 Python 对象 x，complex(x) 会委托给 x.__complex__()。 如果 __complex__() 未定义则将回退至 __float__()。 如果 __float__() 未定义则将回退至 __index__()。

# 对于一个普通 Python 对象 x，complex(x) 会委托给 x.__complex__()。 如果 __complex__() 未定义则将回退至 __float__()。 如果 __float__() 未定义则将回退至 __index__()。
class C:
    # def __complex__(self):
    #     return 1+2j
    # def __float__(self):
    #     return 1.23
    def __index__(self):
        return 123
print('---------')
print(f'{ complex(C()) = }')

#
# 注解 当从字符串转换时，字符串在 + 或 - 的周围必须不能有空格。例如 complex('1+2j') 是合法的，但 complex('1 + 2j') 会触发 ValueError 异常。
print('--------')
print(f'{ complex("1+2j") = }')
print(f'{ complex("-1-2j") = }')
# print(f'{ complex("1+ 2j") = }')


# 数字类型 --- int, float, complex 描述了复数类型。
#
# 在 3.6 版更改: 您可以使用下划线将代码文字中的数字进行分组。
#
# 在 3.8 版更改: 如果 __complex__() 和 __float__() 未定义则回退至 __index__()