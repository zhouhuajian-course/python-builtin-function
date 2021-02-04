open
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# ---- 第1个参数 file ----
# 打开 file 并返回对应的 file object。
# file 是一个 path-like object，表示将要打开的文件的路径（绝对路径或者当前工作目录的相对路径），也可以是要被封装的整数类型文件描述符。
print(f'{ open("test.txt") = }')
abs_path = r"C:\Users\zhouhuajian\PythonProjects\BuiltinFunction\test.txt"
print(f'{ open(abs_path) = }')
print('--------')
import os
print(f'{ os.open("test.txt", os.O_RDONLY) = }')
print(f'{ open(os.open("test.txt", os.O_RDONLY)) = }')

# ---- 第2个参数 mode 文件打开模式 默认值'r' -----
# mode 是一个可选字符串，用于指定打开文件的模式。默认值是 'r' ，这意味着它以文本模式打开并读取。
# 默认模式为 'r' (打开用于读取文本，与 'rt' 同义)。
print('-----------')
print(f'{ open("test.txt") = }')
print(f'{ open("test.txt", mode="r") = }')
print(f'{ open("test.txt", mode="rt") = }')
print(f'{ open("test.txt", mode="rt").read() = }')

# ---- 第3个参数 buffering 缓冲策略 默认值-1 -------
# buffering 是一个可选的整数，用于设置缓冲策略。传递0以切换缓冲关闭（仅允许在二进制模式下），1选择行缓冲（仅在文本模式下可用），并且>1的整数以指示固定大小的块缓冲区的大小（以字节为单位）。如果没有给出 buffering 参数，则默认缓冲策略的工作方式如下:
# 二进制文件以固定大小的块进行缓冲；使用启发式方法选择缓冲区的大小，尝试确定底层设备的“块大小”或使用 io.DEFAULT_BUFFER_SIZE。在许多系统上，缓冲区的长度通常为4096或8192字节。
# “交互式”文本文件（ isatty() 返回 True 的文件）使用行缓冲。其他文本文件使用上述用于二进制文件的策略。
print('--------')
# f = open("test-2.txt", mode="wt")
f = open("test-2.txt", mode="wt", buffering=1)
# print(f'{ f.isatty() = }')  # 不是“交互式”文本文件
# f.write("test test test\n")
f.write("test1 test2 test3\n")
import time
print(" 暂停了10秒 ")
# time.sleep(10)
f.close()

# ---- 第4个参数 encoding 文件读写的字符编码 默认是None ------
# 在文本模式，如果 encoding 没有指定，则根据平台来决定使用的编码：使用 locale.getpreferredencoding(False) 来获取本地编码。
print('-------------')
import locale
print(f'{ locale.getpreferredencoding(False) = }')  # cp936 GBK
print(f'{ open("test.txt") = }')
print(f'{ open("test.txt", encoding="cp936") = }')
print(f'{ open("test.txt", encoding="cp936").read() = }')
# GBK编码来读取UTF-8编码的内容 出现乱码
print(f'{ open("test.txt", encoding="utf-8").read() = }')

# --- 第5个参数 errors 指定如何处理编码和解码错误 默认值None -----
# errors 是一个可选的字符串参数，用于指定如何处理编码和解码错误 - 这不能在二进制模式下使用。可以使用各种标准错误处理程序（列在 错误处理方案 ），但是使用 codecs.register_error() 注册的任何错误处理名称也是有效的。标准名称包括:
# 如果存在编码错误，'strict' 会引发 ValueError 异常。 默认值 None 具有相同的效果。
# 'ignore' 忽略错误。请注意，忽略编码错误可能会导致数据丢失。
# 'replace' 会将替换标记（例如 '?' ）插入有错误数据的地方。
# 'surrogateescape' 将表示任何不正确的字节作为Unicode专用区中的代码点，范围从U+DC80到U+DCFF。当在写入数据时使用 surrogateescape 错误处理程序时，这些私有代码点将被转回到相同的字节中。这对于处理未知编码的文件很有用。
# 只有在写入文件时才支持 'xmlcharrefreplace'。编码不支持的字符将替换为相应的XML字符引用 &#nnn;。
# 'backslashreplace' 用Python的反向转义序列替换格式错误的数据。
# 'namereplace' （也只在编写时支持）用 \N{...} 转义序列替换不支持的字符。
print('------------')
# print(f'{ open("test-3.txt", encoding="cp936").read() = }')
# print(f'{ open("test-3.txt", encoding="cp936", errors="strict").read() = }')
# UnicodeDecodeError
print(f'{ open("test-3.txt", encoding="cp936", errors="ignore").read() = }')

# --- 第6个参数 newline 换行模式 默认值None ----
# newline 控制 universal newlines 模式如何生效（它仅适用于文本模式）。它可以是 None，''，'\n'，'\r' 和 '\r\n'。它的工作原理:
# 从流中读取输入时，如果 newline 为 None，则启用通用换行模式。输入中的行可以以 '\n'，'\r' 或 '\r\n' 结尾，这些行被翻译成 '\n' 在返回调用者之前。如果它是 ''，则启用通用换行模式，但行结尾将返回给调用者未翻译。如果它具有任何其他合法值，则输入行仅由给定字符串终止，并且行结尾将返回给未调用的调用者。
# 将输出写入流时，如果 newline 为 None，则写入的任何 '\n' 字符都将转换为系统默认行分隔符 os.linesep。如果 newline 是 '' 或 '\n'，则不进行翻译。如果 newline 是任何其他合法值，则写入的任何 '\n' 字符将被转换为给定的字符串。
print('-----------')
print(f'{ open("test-4.txt", mode="rb").read() = }')  # \r\n
print(f'{ open("test-4.txt", newline=None).read() = }')
print(f'{ open("test-4.txt", newline="").read() = }')

# ---- 第7个参数 closefd 指定文件关闭时，是否关闭文件描述符 默认值True ----
# file 是一个 path-like object，表示将要打开的文件的路径（绝对路径或者当前工作目录的相对路径），也可以是要被封装的整数类型文件描述符。（如果是文件描述符，它会随着返回的 I/O 对象关闭而关闭，除非 closefd 被设为 False 。）
print('------------')
import os
fd = os.open("test-4.txt", os.O_RDONLY)
# f = open(fd, closefd=True)
f = open(fd, closefd=False)
f.close()
print(f'{ os.read(fd, 1024) = }')  # bytes

# ----- 第8个参数 opener 指定自定义文件打开器 默认值None ------
# 可以通过传递可调用的 opener 来使用自定义开启器。然后通过使用参数（ file，flags ）调用 opener 获得文件对象的基础文件描述符。 opener 必须返回一个打开的文件描述符（使用 os.open as opener 时与传递 None 的效果相同）。
print('-------')
import os
print(f'{ open("test-4.txt", opener=os.open) = }')
def another_opener(file, flags):
    print(f'{ file = }')
    print(f'{ flags = }')
    return os.open(file, flags)
print('---------')
print(f'{ open("test-4.txt", mode="r", opener=another_opener) = }')
print('--------')
print(f'{ open("test-4.txt", mode="r", opener=another_opener).read() = }')

# 两个注意点：
# 1. 上面提供的很多例子为了方便，都没调用f.close()进行关闭文件，释放系统资源。大家正常编程开发时，操作完文件后，要及时f.close()进行关闭文件，释放系统资源
# 2. 如果大家在实际开发中需要调用open()，推荐大家使用with语句的打开文件，自动关闭文件
# with open(...) as f:
#     f.read()
#     f.write()

# 打开 file 并返回对应的 file object。 如果该文件不能被打开，则引发 OSError。 请参阅 读写文件 获取此函数的更多用法示例。
#
# file 是一个 path-like object，表示将要打开的文件的路径（绝对路径或者当前工作目录的相对路径），也可以是要被封装的整数类型文件描述符。（如果是文件描述符，它会随着返回的 I/O 对象关闭而关闭，除非 closefd 被设为 False 。）
#
# mode 是一个可选字符串，用于指定打开文件的模式。默认值是 'r' ，这意味着它以文本模式打开并读取。其他常见模式有：写入 'w' （截断已经存在的文件）；排它性创建 'x' ；追加写 'a' （在 一些 Unix 系统上，无论当前的文件指针在什么位置，所有 写入都会追加到文件末尾）。
# 在文本模式，如果 encoding 没有指定，则根据平台来决定使用的编码：使用 locale.getpreferredencoding(False) 来获取本地编码。（要读取和写入原始字节，请使用二进制模式并不要指定 encoding。）可用的模式有：
#
# 字符  意义
# 'r'   读取（默认） open for reading (default)
# 'w'   写入，并先截断文件 open for writing, truncating the file first
# 'x'   排它性创建，如果文件已存在则失败
#       open for exclusive creation, failing if the file already exists
# 'a'   写入，如果文件存在则在末尾追加
#       open for writing, appending to the end of the file if it exists
# 'b'   二进制模式 binary mode
# 't'   文本模式（默认） text mode (default)
# '+'   打开用于更新（读取与写入） open for updating (reading and writing)
#
# 默认模式为 'r' (打开用于读取文本，与 'rt' 同义)。 模式 'w+' 与 'w+b' 将打开文件并清空内容。 模式 'r+' 与 'r+b' 将打开文件并不清空内容。
#
# 正如在 概述 中提到的，Python区分二进制和文本I/O。以二进制模式打开的文件（包括 mode 参数中的 'b' ）返回的内容为 bytes 对象，不进行任何解码。在文本模式下（默认情况下，或者在 mode 参数中包含 't' ）时，文件内容返回为 str ，首先使用指定的 encoding （如果给定）或者使用平台默认的的字节编码解码。
#
# 此外还允许使用一个模式字符 'U'，该字符已不再具有任何效果，并被视为已弃用。 之前它会在文本模式中启用 universal newlines，这在 Python 3.0 中成为默认行为。 请参阅 newline 形参的文档了解更多细节。
#
# 注解 Python不依赖于底层操作系统的文本文件概念;所有处理都由Python本身完成，因此与平台无关。
# buffering 是一个可选的整数，用于设置缓冲策略。传递0以切换缓冲关闭（仅允许在二进制模式下），1选择行缓冲（仅在文本模式下可用），并且>1的整数以指示固定大小的块缓冲区的大小（以字节为单位）。如果没有给出 buffering 参数，则默认缓冲策略的工作方式如下:
#
# 二进制文件以固定大小的块进行缓冲；使用启发式方法选择缓冲区的大小，尝试确定底层设备的“块大小”或使用 io.DEFAULT_BUFFER_SIZE。在许多系统上，缓冲区的长度通常为4096或8192字节。
#
# “交互式”文本文件（ isatty() 返回 True 的文件）使用行缓冲。其他文本文件使用上述用于二进制文件的策略。
#
# encoding 是用于解码或编码文件的编码的名称。这应该只在文本模式下使用。默认编码是依赖于平台的（不 管 locale.getpreferredencoding() 返回何值），但可以使用任何Python支持的 text encoding 。有关支持的编码列表，请参阅 codecs 模块。
#
# errors 是一个可选的字符串参数，用于指定如何处理编码和解码错误 - 这不能在二进制模式下使用。可以使用各种标准错误处理程序（列在 错误处理方案 ），但是使用 codecs.register_error() 注册的任何错误处理名称也是有效的。标准名称包括:
#
# 如果存在编码错误，'strict' 会引发 ValueError 异常。 默认值 None 具有相同的效果。
#
# 'ignore' 忽略错误。请注意，忽略编码错误可能会导致数据丢失。
#
# 'replace' 会将替换标记（例如 '?' ）插入有错误数据的地方。
#
# 'surrogateescape' 将表示任何不正确的字节作为Unicode专用区中的代码点，范围从U+DC80到U+DCFF。当在写入数据时使用 surrogateescape 错误处理程序时，这些私有代码点将被转回到相同的字节中。这对于处理未知编码的文件很有用。
#
# 只有在写入文件时才支持 'xmlcharrefreplace'。编码不支持的字符将替换为相应的XML字符引用 &#nnn;。
#
# 'backslashreplace' 用Python的反向转义序列替换格式错误的数据。
#
# 'namereplace' （也只在编写时支持）用 \N{...} 转义序列替换不支持的字符。
#
# newline 控制 universal newlines 模式如何生效（它仅适用于文本模式）。它可以是 None，''，'\n'，'\r' 和 '\r\n'。它的工作原理:
#
# 从流中读取输入时，如果 newline 为 None，则启用通用换行模式。输入中的行可以以 '\n'，'\r' 或 '\r\n' 结尾，这些行被翻译成 '\n' 在返回调用者之前。如果它是 ''，则启用通用换行模式，但行结尾将返回给调用者未翻译。如果它具有任何其他合法值，则输入行仅由给定字符串终止，并且行结尾将返回给未调用的调用者。
#
# 将输出写入流时，如果 newline 为 None，则写入的任何 '\n' 字符都将转换为系统默认行分隔符 os.linesep。如果 newline 是 '' 或 '\n'，则不进行翻译。如果 newline 是任何其他合法值，则写入的任何 '\n' 字符将被转换为给定的字符串。
#
# 如果 closefd 是 False 并且给出了文件描述符而不是文件名，那么当文件关闭时，底层文件描述符将保持打开状态。如果给出文件名则 closefd 必须为 True （默认值），否则将引发错误。
#
# 可以通过传递可调用的 opener 来使用自定义开启器。然后通过使用参数（ file，flags ）调用 opener 获得文件对象的基础文件描述符。 opener 必须返回一个打开的文件描述符（使用 os.open as opener 时与传递 None 的效果相同）。
#
# 新创建的文件是 不可继承的。
#
# 下面的示例使用 os.open() 函数的 dir_fd 的形参，从给定的目录中用相对路径打开文件:
#
# >>>
# >>> import os
# >>> dir_fd = os.open('somedir', os.O_RDONLY)
# >>> def opener(path, flags):
# ...     return os.open(path, flags, dir_fd=dir_fd)
# ...
# >>> with open('spamspam.txt', 'w', opener=opener) as f:
# ...     print('This will be written to somedir/spamspam.txt', file=f)
# ...
# >>> os.close(dir_fd)  # don't leak a file descriptor
# open() 函数所返回的 file object 类型取决于所用模式。 当使用 open() 以文本模式 ('w', 'r', 'wt', 'rt' 等) 打开文件时，它将返回 io.TextIOBase (特别是 io.TextIOWrapper) 的一个子类。 当使用缓冲以二进制模式打开文件时，返回的类是 io.BufferedIOBase 的一个子类。 具体的类会有多种：在只读的二进制模式下，它将返回 io.BufferedReader；在写入二进制和追加二进制模式下，它将返回 io.BufferedWriter，而在读/写模式下，它将返回 io.BufferedRandom。 当禁用缓冲时，则会返回原始流，即 io.RawIOBase 的一个子类 io.FileIO。
#
# 另请参阅文件操作模块，例如 fileinput、io （声明了 open()）、os、os.path、tempfile 和 shutil。
#
# 引发一个 审计事件 open 附带参数 file, mode, flags。
#
# mode 与 flags 参数可以在原始调用的基础上被修改或传递。
#
# 在 3.3 版更改:
# 增加了 opener 形参。
#
# 增加了 'x' 模式。
#
# 过去触发的 IOError，现在是 OSError 的别名。
#
# 如果文件已存在但使用了排它性创建模式（ 'x' ），现在会触发 FileExistsError。
#
# 在 3.4 版更改:
# 文件现在禁止继承。
#
# Deprecated since version 3.4, will be removed in version 3.10: 'U' 模式。
#
# 在 3.5 版更改:
# 如果系统调用被中断，但信号处理程序没有触发异常，此函数现在会重试系统调用，而不是触发 InterruptedError 异常（原因详见 PEP 475）。
#
# 增加了 'namereplace' 错误处理接口。
#
# 在 3.6 版更改:
# 增加对实现了 os.PathLike 对象的支持。
#
# 在 Windows 上，打开一个控制台缓冲区将返回 io.RawIOBase 的子类，而不是 io.FileIO。