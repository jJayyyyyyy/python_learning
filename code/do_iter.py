#可以for的数据类型
#集合数据类型: list, tuple, dict, set, str
#generator, 包括生成器和 带yield的generator function
#这些可以直接作用于for的对象统称为可迭代对象 Iterable

from collections import Iterable
#list
print(isinstance([], Iterable))
#dict
print(isinstance({}, Iterable))
#str
print(isinstance('abc', Iterable))
#list_comprehension
print(isinstance([x for x in range(10)], Iterable))
#generator
print(isinstance((x for x in range(10)), Iterable))
#int
print(isinstance(100, Iterable))
print()

#生成器不但可以作用于for循环，还可以被next()函数多次调用
#可以被next()函数调用并不断返回下一个值的对象
#称为迭代器：Iterator
from collections import Iterator
#list_comprehension
print(isinstance((x for x in range(5)), Iterator))
#list
print(isinstance([], Iterator))
#dict
print(isinstance({}, Iterator))
#str
print(isinstance('abc', Iterator))
print()

#生成器都是Iterator对象，
#但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter('abc'), Iterator))






'''
小节
Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用
并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，
所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。
而使用list是永远不可能存储全体自然数的
'''


#Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass

#实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

