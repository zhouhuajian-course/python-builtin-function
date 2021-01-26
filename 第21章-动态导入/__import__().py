# __import__(name, globals=None, locals=None, fromlist=(), level=0)
# __import__
# 注解 与 importlib.import_module() 不同，这是一个日常 Python 编程中不需要用到的高级函数。
# 此函数会由 import 语句发起调用。 它可以被替换 (通过导入 builtins 模块并赋值给 builtins.__import__) 以便修改 import 语句的语义，但是 强烈 不建议这样做，因为使用导入钩子 (参见 PEP 302) 通常更容易实现同样的目标，并且不会导致代码问题，因为许多代码都会假定所用的是默认实现。 同样也不建议直接使用 __import__() 而应该用 importlib.import_module()。

# 此函数会由 import 语句发起调用。 它可以被替换 (通过导入 builtins 模块并赋值给 builtins.__import__) 以便修改 import 语句的语义，

import builtins
# builtins.__import__ = print
# import cat
# 等价于
# cat = __import__('cat', globals(), locals(), None, 0)
# cat.run()
# # spam = __import__('spam', globals(), locals(), [], 0)

# 当 name 变量的形式为 package.module 时，通常将会返回最高层级的包（第一个点号之前的名称），而 不是 以 name 命名的模块。
# import animal.cat.behaviour
# 等价于
# animal = __import__('animal.cat.behaviour', globals(), locals(), None, 0)
# print(animal.__name__)
# print(dir())

# 但是，当给出了非空的 fromlist 参数时，则将返回以 name 命名的模块。
# builtins.__import__ = print
# from animal.cat import behaviour
# _temp = __import__('animal.cat', globals(), locals(), ('behaviour',), 0)
# behaviour = _temp.behaviour
# behaviour.run()
# print(f'{ _temp = }')
# _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
# eggs = _temp.eggs
# saus = _temp.sausage
# 在这里， spam.ham 模块会由 __import__() 返回。 要导入的对象将从此对象中提取并赋值给它们对应的名称。

# level 指定是使用绝对还是相对导入。 0 (默认值) 意味着仅执行绝对导入。 level 为正数值表示相对于模块调用 __import__() 的目录，将要搜索的父目录层数 (详情参见 PEP 328)。
import animal.human.behaviour
animal.human.behaviour.dance()

# import name
# 等价于__import__(name, globals(), locals(), None, 0)
# from name import name1, name2, name3
# 等价于__import__(name, globals(), locals(), (name1, name2, name3), 0)
# from .name import name1, name2, name3
# 等价于__import__(name, globals(), locals(), (name1, name2, name3), 1)
# from ..name import name1, name2, name3
# 等价于__import__(name, globals(), locals(), (name1, name2, name3), 2)
# level为0绝对导入，相对导入时，level为小点的数量

# 该函数会导入 name 模块，有可能使用给定的 globals 和 locals 来确定如何在包的上下文中解读名称。 fromlist 给出了应该从由 name 指定的模块导入对象或子模块的名称。 标准实现完全不使用其 locals 参数，而仅使用 globals 参数来确定 import 语句的包上下文。
#
# level 指定是使用绝对还是相对导入。 0 (默认值) 意味着仅执行绝对导入。 level 为正数值表示相对于模块调用 __import__() 的目录，将要搜索的父目录层数 (详情参见 PEP 328)。
#
# 当 name 变量的形式为 package.module 时，通常将会返回最高层级的包（第一个点号之前的名称），而 不是 以 name 命名的模块。 但是，当给出了非空的 fromlist 参数时，则将返回以 name 命名的模块。
#
# 例如，语句 import spam 的结果将为与以下代码作用相同的字节码:
#
# spam = __import__('spam', globals(), locals(), [], 0)
# 语句 import spam.ham 的结果将为以下调用:
#
# spam = __import__('spam.ham', globals(), locals(), [], 0)
# 请注意在这里 __import__() 是如何返回顶层模块的，因为这是通过 import 语句被绑定到特定名称的对象。
#
# 另一方面，语句 from spam.ham import eggs, sausage as saus 的结果将为
#
# _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
# eggs = _temp.eggs
# saus = _temp.sausage
# 在这里， spam.ham 模块会由 __import__() 返回。 要导入的对象将从此对象中提取并赋值给它们对应的名称。
#
# 如果您只想按名称导入模块（可能在包中），请使用 importlib.import_module()
#
# 在 3.3 版更改: level 的值不再支持负数（默认值也修改为0）。
#
# 在 3.9 版更改: 当使用了命令行参数 -E 或 -I 时，环境变量 PYTHONCASEOK 现在将被忽略。
