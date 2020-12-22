# round(number[, ndigits])
# 返回 number 舍入到小数点后 ndigits 位精度的值。 如果 ndigits 被省略或为 None，则返回最接近输入值的整数。
#
# 返回 number 舍入到小数点后 ndigits 位精度的值。
print(f'{ round(123.456, 2) = }')
# 如果 ndigits 被省略或为 None，则返回最接近输入值的整数。
print(f'{ round(123.456) = }')
print(f'{ round(123.456, None) = }')

# 对于支持 round() 的内置类型，值会被舍入到最接近的 10 的负 ndigits 次幂的倍数；如果与两个倍数的距离相等，则选择偶数 (因此，round(0.5) 和 round(-0.5) 均为 0 而 round(1.5) 为 2)。 任何整数值都可作为有效的 ndigits (正数、零或负数)。 如果 ndigits 被省略或为 None 则返回值将为整数。 否则返回值与 number 的类型相同。

# 对于支持 round() 的内置类型，值会被舍入到最接近的 10 的负 ndigits 次幂的倍数；如果与两个倍数的距离相等，则选择偶数 (因此，round(0.5) 和 round(-0.5) 均为 0 而 round(1.5) 为 2)。
numbers = [-0.5, 0.5, 1.5, 2.5, 3.5]
for num in numbers:
    print(f'{ num = } { round(num) = }')
print(f'{ round(0.125, 2) = }')
print(f'{ round(0.51) = }')
print(f'{ round(0.1251, 2) = }')
# round()内置函数不是使用四舍五入的规则，而是根据距离远近的规则来取近似值
# 四舍六入五考虑 或者 四舍六入五平分
# 如果小于等于4则舍去，如果大于等于6则进入。如果5后面还有有效数字，则进1，如果5后面没有有效数字，则选择偶数

# 任何整数值都可作为有效的 ndigits (正数、零或负数)。
print(f'{ round(123.456, 2) = }')
print(f'{ round(123.456, 0) = }')
print(f'{ round(123.456, -2) = }')
print(f'{ round(163.456, -2) = }')
# 如果 ndigits 被省略或为 None 则返回值将为整数。 否则返回值与 number 的类型相同。
print(f'{ round(123.456) = }')
print(f'{ round(123.456, None) = }')
print(f'{ round(123.456, 2) = }')

#
# 对于一般的 Python 对象 number, round 将委托给 number.__round__。

# 对于一般的 Python 对象 number, round 将委托给 number.__round__。
print(f'{ round(123.456, 2) = }')
print(f'{ 123.456.__round__(2) = }')
#
# 注解 对浮点数执行 round() 的行为可能会令人惊讶：例如，round(2.675, 2) 将给出 2.67 而不是期望的 2.68。 这不算是程序错误：这一结果是由于大多数十进制小数实际上都不能以浮点数精确地表示。 请参阅 浮点算术：争议和限制 了解更多信息。

# 注解 对浮点数执行 round() 的行为可能会令人惊讶：例如，round(2.675, 2) 将给出 2.67 而不是期望的 2.68。 这不算是程序错误：这一结果是由于大多数十进制小数实际上都不能以浮点数精确地表示。
print(f'{ round(2.675, 2) = }')
print(f'{ round(0.125, 2) = }')


