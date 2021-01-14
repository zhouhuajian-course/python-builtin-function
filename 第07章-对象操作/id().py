# id(object)
# 返回对象的“标识值”。该值是一个整数，在此对象的生命周期中保证是唯一且恒定的。两个生命期不重叠的对象可能具有相同的 id() 值。
#
# CPython implementation detail: This is the address of the object in memory.
#
# 引发一个 审计事件 builtins.id，附带参数 id。

# 返回对象的“标识值”。该值是一个整数，在此对象的生命周期中保证是唯一且恒定的。
# This is the address of the object in memory.
list_test = ["a", "b"]
print(f'{ id(list_test) = }')
print(f'{ hex(id(list_test)) = }')
str_test = "ab"
print(f'{ id(str_test) = }')
print(f'{ hex(id(str_test)) = }')
print('-------')
list_test.append("c")
print(f'{ id(list_test) = }')
str_test += "c"
print(f'{ id(str_test) = }')
# 引发一个 审计事件 builtins.id，附带参数 id。
import sys
def audit_hook(event, args):
    if event in ['builtins.id']:
        print(f'{ event = } { args = }')
sys.addaudithook(audit_hook)
print('------')
print(f'{ id("测试") = }')