#待理解


#函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
	print('2016')
f = now
f()

#函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)
print()


#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
#但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

#本质上，decorator就是一个返回函数的高阶函数。
#所以，我们要定义一个能打印日志的decorator，可以定义如下
def log(func):
	#可变参数的写法 def f(*args),参数接收数量可变
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数
#我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
	print('2016')

now()
print()
#把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)

#wrapper()函数的参数定义是(*args, **kw)
#因此，wrapper()函数可以接受任意参数的调用
#def f(*args, **kw):
#	print(args, kw)
#f(1, 2, 3, 'a', [1, 2])


#如果decorator本身需要传入参数，
#那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
#比如，要自定义log的文本
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

#这个3层嵌套的decorator用法如下
@log('execute')
def now():
	print('2016')

now()



#一个完整的decorator的写法如下
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

#或者针对带参数的decorator
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#作业
