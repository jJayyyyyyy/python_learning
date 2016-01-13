# -*- coding: utf-8 -*-

#默认参数
def power(x, n=2):
	s = 1
	while n > 0:
		s = s * x
		n = n - 1
	return s
print(power(2, 3))
print(power(2))

def enroll(name, gender, age=7, city='SH'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city, '\n')

enroll('Ljj', 'Boy')
enroll('Bob', 'Boy', 6)
enroll('Sarah', 'Girl', city='BK')

def add_end(L=None):
	#None是不变对象
	if L is None:
		L = []
	L.append('END')
	return L

#可变参数
def cacl(*number):
	sum = 0
	for n in number:
		sum += n
	return sum
print(cacl())
print(cacl(1))
print(cacl(1, 2))
nums1=(1, 2, 3)
print(cacl(*nums1))
nums2=[1, 2, 3, 4]
print(cacl(*nums2))
print('\n\n')


#关键字参数,用于扩展函数的功能
def person(name, age, **keyWord):
	print('name:', name, 'age:', age, 'other:', keyWord)
print(person('Michael', 30))
print(person('Bob', 35, city='Beijing'))
print(person('Adam', 40, gender='M', job='Engineer'))
extra={'city':'Beijing', 'job':'Pilot'}
print(person('Ali', 24, **extra))
print('\n\n')

#命名关键字参数,只接收city和job作为关键字参数
def person2(name, age, *, city, job):
	print(name, age, city, job)
print(person2('Jack', 24, city='Beijing', job='Engineer'))

#必选参数、默认参数、可变参数、关键字参数和命名关键字参数
#可变参数(*number) 无法和命名关键字参数(*,) 混合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！




