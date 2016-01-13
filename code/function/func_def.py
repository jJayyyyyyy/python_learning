# -*- coding: utf-8 -*-

def myAbs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x

print(myAbs(-100))

#进入交互环境后
#from func_def import myAbs
#即可调用myAbs()

def nop():
	pass


import math
def move(x, y, length, angle=0):
	nX = x + length*math.cos(angle)
	nY = y + length*math.sin(angle)
	return int(nX), nY

'''
小结
定义函数时，需要确定函数名和参数个数；
如果有必要，可以先对参数的数据类型做检查；
函数体内部可以用return随时返回函数结果；
函数执行完毕也没有return语句时，自动return None。
函数可以同时返回多个值，但其实就是一个tuple。
'''
#练习
def quadratic(a, b, c):
	if not isinstance(a, (int, float)):
		raise TypeError('bad operand type')
	elif not isinstance(b, (int, float)):
		raise TypeError('bad operand type')
	elif not isinstance(c, (int, float)):
		raise TypeError('bad operand type')
	delta_2 = b*b - 4*a*c
	if delta_2 < 0:
		return 'No real Solution!'
	else:
		delta = math.sqrt(delta_2)
		return (-b+delta)/(2*a), (-b-delta)/(2*a)

