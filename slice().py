# class slice(stop)
# class slice(start, stop[, step])
# slice内置函数，本质上是一个类，有两种传参方式
# 第一种是传一个参数stop
# 第二种是传三个参数start, stop和step，其中step是可选的
# Return a slice object representing the set of indices. The start and step arguments default to None.
# 返回表示索引集合的切片对象. start和step参数默认是None
print(f'{ slice(3) = }')
print(f'{ slice(0, 3) = }')
print(f'{ slice(0, 3, 1) = }')
# Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default).
# slice切片对象有只读的数据属性start, stop和step，这三个属性只返回参数值（或者它的默认值）
print('------------')
print(f'{ slice(0, 3).start = }')
print(f'{ slice(0, 3).stop = }')
print(f'{ slice(0, 3).step = }')
print(f'{ slice(0, 3, 1).step = }')
# 步长
# slice(0, 3, 1).step = 2
# They have no other explicit functionality; however they are used by NumPy and other third party packages. Slice objects are also generated when extended indexing syntax is used. For example: a[start:stop:step] or a[start:stop, i].
# slice对象没有其他明确的用途，然而slice对象有被NumPy包和其他第三方包使用。当使用扩展索引语法时，slice对象也会被生成。
class SeqTest:
    def __getitem__(self, key):
        return key
s = SeqTest()
print('-------')
print(f'{ s[:3] = }')
print(f'{ s[0:3] = }')
print(f'{ s[0:3:1] = }')
print('--------')
string = "abcde"
print(f'{ string[1:3] = }')
print(f'{ string[slice(1, 3)] = }')

# Return a slice object representing the set of indices specified by range(start, stop, step).The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default). They have no other explicit functionality; however they are used by NumPy and other third party packages. Slice objects are also generated when extended indexing syntax is used. For example: a[start:stop:step] or a[start:stop, i]. See itertools.islice() for an alternate version that returns an iterator.