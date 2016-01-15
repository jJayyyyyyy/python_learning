print(abs(-10))
print(abs)

f = abs
print(f(-1))

'''
#函数名也可以是变量
abs = 10
abs(-10)
#会出错，因为abs已经指向一个整数10
'''

#高阶函数
#既然变量可以指向函数，函数的参数能接收变量，
#那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, func):
	return func(x)+func(y)
x = -5
y = 6
func = abs
print(add(x, y, func))
print(add(-1, -2, abs))

#编写高阶函数，就是让函数的参数能够接收别的函数
#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
