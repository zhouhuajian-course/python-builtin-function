# class slice(stop)
# class slice(start, stop[, step])
# slice
# 返回一个表示由 range(start, stop, step) 所指定索引集的 slice 对象。 其中 start 和 step 参数默认为 None。 切片对象具有仅会返回对应参数值（或其默认值）的只读数据属性 start, stop 和 step。 它们没有其他的显式功能；不过它们会被 NumPy 以及其他第三方扩展所使用。 切片对象也会在使用扩展索引语法时被生成。 例如: a[start:stop:step] 或 a[start:stop, i]。 请参阅 itertools.islice() 了解返回迭代器的一种替代版本。

# 返回一个表示由 range(start, stop, step) 所指定索引集的 slice 对象。 其中 start 和 step 参数默认为 None。
print(f'{ slice(3) = }')
print(f'{ slice(0, 3) = }')
print(f'{ slice(0, 3, 1) = }')
# 切片对象具有仅会返回对应参数值（或其默认值）的只读数据属性 start, stop 和 step。
print('------')
print(f'{ slice(0, 3, 1).start = }')
print(f'{ slice(0, 3, 1).stop = }')
print(f'{ slice(0, 3, 1).step = }')
# 它们没有其他的显式功能；不过它们会被 NumPy 以及其他第三方扩展所使用。 切片对象也会在使用扩展索引语法时被生成。 例如: a[start:stop:step] 或 a[start:stop, i]。
# slice切片对象主要在Python对序列进行切片时使用
print('---------')
string = "abcd"
print(f'{ string[0:3] = }')
print(f'{ string[0:3:1] = }')
# __getitem__
class Sequence:
    def __getitem__(self, key):
        print(f'{ self = }')
        print(f'{ key = }')
        print(f'{ type(key) = }')
print('-------')
seq = Sequence()
seq[0:3] # seq[0:3] 会转成seq[slice(0, 3, None)]
print('-------')
seq[0:3:1] # seq[0:3:1] 会转成seq[slice(0, 3, 1)]
print('-------')
string = "abcd"
print(f'{ string[0:3] = }')
print(f'{ string[0:3:1] = }')
print(f'{ string[slice(0, 3)] = }')
print(f'{ string[slice(0, 3, 1)] = }')