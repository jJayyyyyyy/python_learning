# -*- coding: utf-8 -*-
#map 分布
def f(x):
	return x*x
r = map(f, [1, 2, 3, 4])
print(list(r))

#map()作为高阶函数，事实上它把运算规则抽象了，我们不但可以计算简单的f(x)=x^2，
#还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
print(list(map(str, [1, 2, 3, 4])))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#比方说对一个序列求和，就可以用reduce实现
from functools import reduce
def add(x, y):
	return x+y
print(reduce(add, [1, 2, 3, 4]))

#当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。
#但如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def fn(x, y):
	return x*10 + y
print(reduce(fn, [1, 2, 3, 4]))

#str也是一个序列，reduce()配合map()把str转换为int也可以如法炮制
def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4}[s]
print(reduce(fn, (map(char2num, '1023'))))

#整理成一个str2int
def str2int(s):
	def fn(x, y):
		return x*10 + y
	def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4}[s]
	return reduce(fn, map(char2num, s))
print(str2int('123'))

#lambda函数进一步简化
def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4}[s]
def str2int(s):
	return reduce(lambda x, y: x*10+y, map(char2num, s))
print(str2int('41'))
print()
print()
#也就是说，假设Python没有提供int()函数，
#你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码


#练习1
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

#提示: print('sTR'.title()), 有python内置的函数不用白不用
#举例：华为机考题2 输入一段英文字符串，将每个单词首字母大写后输出
print('how are you today?'.title())

####练习1
names = ['adam smith. i go!', 'LIsA', 'barT']
#首先定义规则
def pre_normalize(name):
	return name.title()
#然后用map把规则用到每一个身上
def normalize(names):
	return list(map(pre_normalize, names))
print(normalize(names))

#更简单的
names = ['adam', 'LISA', 'barT']
print(list(map(str.title, names)))

#注意，str.title() 与str.upper(), str.lower()还不太一样
L = ['hello world', 'this is google']
def Nor(s):
    return s[0].upper() + s[1:].lower()
print(list(map(Nor, L)))


#练习2
#Python提供的sum()函数可以接受一个list并求和
#请编写一个prod()函数，可以接受一个list并利用reduce()求积
def product(L):
	def multiply(x, y):
		return x*y
	return reduce(multiply, L)
L = [1, 2, 3, 4]
print(product(L))
#print(reduce(multiply, [1, 2, 3, 4]))
print()
print()

#练习3
#利用map和reduce编写一个str2float函数
#把字符串'123.456'转换成浮点数123.456
def str2float(s):
	def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	def mul(x, y):
		return x*10+y
	'''
	#Version_1
		#s1, s2 = s.split('.')
		#num1 = list(map(char2num, s1))
		#num2 = list(map(char2num, s2))
		#print(num1, num2)
		#print(reduce(mul, num1+num2)/pow(10, len(num2)))
	#Version_2
		s1, s2 = s.split('.')
		num1, num2 = map(char2num, s1), map(char2num, s2)
		return reduce(mul, num1)+reduce(mul, num2)/pow(10, len(s2))
	'''
	#Version_3
	s1, s2 = s.split('.')
	return reduce(mul, map(char2num, s1))+reduce(mul, map(char2num, s2))/pow(10, len(s2))
	#lambda
	#s1, s2 = s.split('.')
	#l = lambda x, y: x*10+y
	#return reduce(l, map(char2num, s1))+reduce(l, map(char2num, s2))/pow(10, len(s2))
	#(lambda x, y: x*10+y)代替了(mul)

print(str2float('123.456'))
print(float('123.456'))
'''
s = '123.456'
s1, s2=s.split('.')
print(s1)
'''
