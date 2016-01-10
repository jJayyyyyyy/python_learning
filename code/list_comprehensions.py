#列表生成式即List Comprehensions，
#是Python内置的非常简单却强大的可以用来创建list的表达式

print(list(range(1, 11)))
L=[]
for x in range(1, 11):
	L.append(x*x)
print(L)
print()

#循环太繁琐，列表生成式则可以用一行语句代替循环生成上面的list：
L1 = [x*x for x in range(1, 11)]
print(L1)
#if
L2 = [x*x for x in range(1, 11) if x%2==0]
print(L2)
#两层循环。全排列
L3 = [m+n for m in 'XYZ' for n in 'ABC']
print(L3)
print()


#运用列表生成式，可以写出非常简洁的代码
#例如，列出当前目录下的所有文件和目录名
import os
L4 = [d for d in os.listdir('.')]
print(L4)



