# input([prompt])
# 如果存在 prompt 实参，则将其写入标准输出，末尾不带换行符。接下来，该函数从输入中读取一行，将其转换为字符串（除了末尾的换行符）并返回。当读取到 EOF 时，则触发 EOFError。例如:

# 如果存在 prompt 实参，则将其写入标准输出，末尾不带换行符。
# 接下来，该函数从输入中读取一行，将其转换为字符串（除了末尾的换行符）并返回。
prompt = '请输入内容:'
line = input(prompt)
print(f'{ line = } { type(line) = }')
#
print(prompt, end='')
line = input()
print(f'{ line = } { type(line) = }')

# 当读取到 EOF 时，则触发 EOFError。
while True:
    line = input()
    print(f'{ line = }')
while True:
    try:
        line = input()
        print(f'{ line = }')
    except EOFError:
        break



# >>>
# >>> s = input('--> ')
# --> Monty Python's Flying Circus
# >>> s
# "Monty Python's Flying Circus"
# 如果加载了 readline 模块，input() 将使用它来提供复杂的行编辑和历史记录功能。

# 如果加载了 readline 模块，input() 将使用它来提供复杂的行编辑和历史记录功能。
import readline
history_filepath = 'history.txt'
while True:
    line = input('请输入内容:')
    print(f'{ line = }')
    readline.write_history_file(history_filepath)

#
# 引发一个 审计事件 builtins.input 附带参数 prompt。
#
# 在成功读取输入之后引发一个审计事件 builtins.input/result 附带结果。

# 引发一个 审计事件 builtins.input 附带参数 prompt。
# 在成功读取输入之后引发一个审计事件 builtins.input/result 附带结果。
import sys
def audit_hook(event, args):
    if event in ['builtins.input', 'builtins.input/result']:
        print(f'{ event = } { args = }')
sys.addaudithook(audit_hook)
line = input('请输入内容:')
print(f'{ line = }')