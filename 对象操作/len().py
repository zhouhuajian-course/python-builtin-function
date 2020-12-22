# len(s)
# 返回对象的长度（元素个数）。实参可以是序列（如 string、bytes、tuple、list 或 range 等）或集合（如 dictionary、set 或 frozen set 等）。
#
# CPython implementation detail: len 对于大于 sys.maxsize 的长度如 range(2 ** 100) 会引发 OverflowError。

# 返回对象的长度（元素个数）。实参可以是序列（如 string、bytes、tuple、list 或 range 等）或集合（如 dictionary、set 或 frozen set 等）。
print(f'{ len("abc") = }')
print(f'{ len(bytes("abc", "utf-8")) = }')
print(f'{ len(["a", "b", "c"]) = }')
print(f'{ len(("a", "b", "c")) = }')
print(f'{ len(range(3)) = }')
print('------------')
print(f'{ len({"a":1, "b":2, "c":3}) = }')
print(f'{ len({"a", "b", "c"}) = }')
print(f'{ len(frozenset({"a", "b", "c"})) = }')
# len 对于大于 sys.maxsize 的长度如 range(2 ** 100) 会引发 OverflowError。
print('------------')
import sys
print(f'{ sys.maxsize = }')
print(f'{ 2**100 > sys.maxsize = }')
# print(f'{ len(range(2**100)) = }')