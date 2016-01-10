# -*- coding: utf-8 -*-

#任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型
#只要符合迭代条件，就可以使用for循环。

#迭代 iteration
d = {'a':1, 'b':2, 'c':3}
for k in d:
	print(k)
print()

#判断对象可否迭代
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
print()

#下标循环
for i, value in enumerate(['AA', 'BB', 'CC']):
	print(i, value)
print()
for x, y in [(4, 2), (3, 4), (5, 6)]:
	print(x, y)
	