"""
abs(x)
返回一个数的绝对值。 参数可以是整数、浮点数或任何实现了 __abs__() 的对象。 如果参数是一个复数，则返回它的模
"""
# absolute value
# 返回一个数的绝对值
# 参数可以是整数
print(f'{ abs(123) = }')
print(f'{ abs(-123) = }')
print(f'{ abs(0) = }')
# 参数可以是浮点数
print(f'{ abs(1.23) = }')
print(f'{ abs(-1.23) = }')
print(f'{ abs(0.0) = }')
# 参数可以任何实现了 __abs__() 的对象。
class TestClass:
    def __abs__(self):
        return 123
print(f'{ abs(TestClass()) = }')
# 如果参数是一个复数，则返回它的模
# 复数是实数+虚数
# 注意点：复数的绝对值返回值一定是浮点数
print(f'{ abs(3+4j) = }')
print(f'{ abs(-3-4j) = }')