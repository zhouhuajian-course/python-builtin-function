# callable(object)
# 如果参数 object 是可调用的就返回 True，否则返回 False。 如果返回 True，调用仍可能失败，但如果返回 False，则调用 object 将肯定不会成功。 请注意类是可调用的（调用类将返回一个新的实例）；如果实例所属的类有 __call__() 则它就是可调用的。
#
# 3.2 新版功能: 这个函数一开始在 Python 3.0 被移除了，但在 Python 3.2 被重新加入。

# # 如果参数 object 是可调用的就返回 True，否则返回 False。
print(f'{ callable(callable) = }')
def function():
    pass
print(f'{ callable(function) = }')
print(f'{ callable(123) = }')
print(f'{ callable("test") = }')
# 请注意类是可调用的（调用类将返回一个新的实例）；
print('--------')
class C:
    pass
print(f'{ callable(C) = }')
# 如果实例所属的类有 __call__() 则它就是可调用的。
print(f'{ callable(C()) = }')
print('--------')
class C:
    def __call__(self):
        return "test"
print(f'{ callable(C()) = }')
print(f'{ C()() = }')
