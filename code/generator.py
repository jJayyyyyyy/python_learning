#按照某种算法，在循环的过程中不断推算出后续的元素
#这样就不必创建完整的list，从而节省大量的空间
#在Python中，这种一边循环一边计算的机制，称为生成器：generator
import os
g = (doc for doc in os.listdir('.'))
print(next(g))
print()
for n in g:
	print(n)

print()
#我们创建了一个generator后，基本上永远不会调用next()
#而是通过for循环来迭代它，并且不需要关心StopIteration的错误


#斐波拉契数列（Fibonacci）
#用列表生成式写不出来，但是，用函数把它打印出来却很容易
def fib(max):
	n, a, b = 0, 0, 1
	while n<max:
		print(b)		
		#卧槽。。还能这样玩。。
		a, b = b, a+b
		n += 1
	return 'done'
print(fib(5))
print()
'''
仔细观察可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，
可以从第一个元素开始，推算出后续任意的元素，
这种逻辑其实非常类似generator。
也就是说，上面的函数和generator仅一步之遥。
要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
'''
def fib_gen(max):
	n, a, b = 0, 0, 1
	while n<max:
		yield b
		a, b = b, a+b
		n += 1
	return 'done'
#这就是定义generator的另一种方法。
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，
#而是一个generator：
print(fib_gen(5))
for n in fib_gen(5):
	print(n)
print()
#变成generator的函数，在每次调用next()的时候执行
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
#有点像 <中断>
#如下
def odd():
	print('Step 1')
	yield 1
	print('Step 2')
	yield 3
	print('Step 3')
	yield 5
o = odd()
print(next(o))
print(next(o))
print(next(o))
#next(o)
#也就是再次odd()时，不会Step 1 了，而是Step 2

#如果想要拿到返回值，必须捕获StopIteration错误
g = fib_gen(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as error:
		print('Generator retur value:', error.value)
		break

#tips: #Python中，可以简单地把列表生成式改成generator
#也可以通过函数实现复杂逻辑的generator

#理解generator的原理，它在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
#对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。


#homework: 杨辉三角
def triangles():
	pass











