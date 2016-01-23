#当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
#首先,基本类型都可以用type()判断
print(type(123))
print(type('st'))

#如果指向一个函数或者类，也可以用
print(type(abs))
class Animal(object):
	pass
a = Animal()
print(type(a))

#返回的类型，在if判断的时候用到
#1. 判断一个对象是否为函数
#自建函数
import types
def fn():
	pass
print(type(fn) == types.FunctionType)
#内置函数
print(type(abs) == types.BuiltinFunctionType)
#lambda
print(type(lambda x:x) == types.LambdaType)
#生成器
print(type((x for x in range(10))) == types.GeneratorType)
print()


#使用 isinstance()
#对于class 的继承关系来说，使用type()就很不方便
#要判断class 的类型，可以用isinstance()
#object -> Animal -> Dog -> Husky
a = Animal()

class Dog(Animal):
	pass
b = Dog()

class Husky(Dog):
	pass
h = Husky()
print(isinstance(h, Husky))
print(isinstance(h, Dog))
#也没有问题
print(isinstance(h, Animal))


#能用type()判断的基本类型也可以用isinstance()判断
print(isinstance('a', str))
print(isinstance(b'a', bytes))
print()

#还可以判断一个变量是不是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))


#使用dir(), 获得一个对象的所有属性和方法
#比如获得一个str对象的所有属性和方法
print(dir('Abc'))
print()


#类似__xxx__的属性和方法在python中都是有特殊用途的
#比如__len__
print(len('abc'))
print('abc'.__len__())
#两者等价
#因此，如果自己写的类也想用len()方法，那就写一个
#注意写法
class MyRuler(object):
	def __len__(self):
		return 100

ruler = MyRuler()
print(len(ruler))
print()

#其他的
print('A'.lower())

#配合getchar(), setattr(), 以及hasattr(),
#可以直接操作一个对象的状态
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
print()

#如果试图获取不存在的属性，会抛出AttributeError
#print(getattr(obj, 'z'))
#可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404))
#以后会用到

#也可以获得对象的方法
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())


#小结
'''
通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
如果可以直接写：
sum = obj.x + obj.y
就不要写：
sum = getattr(obj, 'x') + getattr(obj, 'y')
'''

#一个正确的用法
def readImage(fp):
	if hasattr(fp, 'read'):
		return readData(fp)
	return None

'''
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
如果存在，则该对象是一个流，如果不存在，则无法读取。
hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，
不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，
但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''


