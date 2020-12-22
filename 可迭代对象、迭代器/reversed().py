# reversed(seq)
# 返回一个反向的 iterator。 seq 必须是一个具有 __reversed__() 方法的对象或者是支持该序列协议（具有从 0 开始的整数类型参数的 __len__() 方法和 __getitem__() 方法）。
print(f'{ hasattr(list, "__reversed__") = }')
print(f'{ reversed(["a", "b", "c"]) = }')
print(f'{ list(reversed(["a", "b", "c"])) = }')
print('----------------')
print(f'{ hasattr(tuple, "__reversed__") = }')
print(f'{ hasattr(tuple, "__len__") = }')
print(f'{ hasattr(tuple, "__getitem__") = }')
print(f'{ reversed(("a", "b", "c")) = }')
print(f'{ tuple(reversed(("a", "b", "c"))) = }')
print('------------------')
print(f'{ hasattr(range, "__reversed__") = }')
print(f'{ reversed(range(3)) = }')
print(f'{ list(reversed(range(3))) = }')
print('----------------')
print(f'{ hasattr(str, "__reversed__") = }')
print(f'{ hasattr(str, "__len__") = }')
print(f'{ hasattr(str, "__getitem__") = }')
print(f'{ reversed("abc") = }')
print(f'{ list(reversed("abc")) = }')
