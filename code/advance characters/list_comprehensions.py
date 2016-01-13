#列表生成式即List Comprehensions，
#是Python内置的非常简单却强大的可以用来创建list的表达式

#普通
print(list(range(1, 11)))
L=[]
for x in range(1, 11):
	L.append(x*x)
print(L)
print()
#循环太繁琐

#列表生成式则可以用一行语句代替循环生成上面的list：
L1 = [x*x for x in range(1, 11)]
print(L1)
#if筛选
L2 = [x*x for x in range(1, 11) if x%2==0]
print(L2)
#两层循环。全排列 (字符串)
L3 = [m+n for m in 'XYZ' for n in 'ABC']
print(L3)
print()


#运用列表生成式，可以写出非常简洁的代码
#例如，列出当前目录下的所有文件和目录名
import os
print([doc for doc in os.listdir('.')])
print()

#多个变量
#循环
d = {'x':'A', 'y':'B', 'z':'C'}
for k, v in d.items():
	print(k, '=', v)
#列表生成式
print([k+'='+v for k, v in d.items()])

#把一个list中所有的字符串变成小写
L = ['HELLO', 'WORLD']
print([s.lower() for s in L])
print()


#练习
L2 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L2 if isinstance(s, str)])
#作业区的一个问题，str不能当做变量并赋值
#如 str='a' 之后，str便失去原来意义
