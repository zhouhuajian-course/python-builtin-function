# ord(c)
# 对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。例如 ord('a') 返回整数 97， ord('€') （欧元符号）返回 8364 。这是 chr() 的逆函数

# 对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。
print(f'{ ord("A") = }')
print(f'{ ord("a") = }')
print(f'{ ord("©") = }')
print(f'{ ord("汉") = }')
print(f'{ ord("😎") = }')
print(f'{ ord("🐈") = }')
# 这是 chr() 的逆函数
print(f'{ ord(chr(128008)) = }')
# 注意点：必须传一个字符的字符串，如果传空字符串或多个字符的字符串会报类型错误
# print(f'{ ord("") = }')
print(f'{ ord("ab") = }')