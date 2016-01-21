#继承和多态
#当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass）
#而被继承的class称为基类、父类或超类（Base class、Super class）

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def eat(self):
		print('Eating...')

class Cat(Animal):
	def run(self):
		print('Chasing a mouse...')

dog = Dog()
dog.run()
#当子类和父类都存在相同的run()方法时，子类的run()会覆盖父类的run()
cat = Cat()
cat.run()
#我们就获得了继承的另一个好处：多态
#要理解什么是多态，我们首先要对数据类型再作一点说明。
#当我们定义一个class的时候，我们实际上就定义了一种数据类型
a = list()		#a是list类型
b = Animal()	#b是Animal类型
c = Dog()		#c是Dog类型
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
#而且
print(isinstance(c, Animal))
#所以，在继承关系中，如果一个实例的数据类型是某个子类，
#那它的数据类型也可以被看做是父类。但是，反过来就不行
print(isinstance(b, Dog))
print()

#要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量
def run_twice(animal):
	animal.run()
	animal.run()
#当我们传入Animal的实例时，run_twice()就打印出
run_twice(Animal())
run_twice(Cat())

#你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，
#实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，
#原因就在于多态



'''
多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，
就会自动调用实际类型的run()方法，这就是多态的意思

对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，
就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat
还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：
调用方只管调用，不管细节，而当我们新增一种Animal的子类时，
只要确保run()方法编写正确，不用管原来的代码是如何调用的。

这就是著名的“开闭”原则：
对扩展开放：允许新增Animal子类
对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
'''


#静态语言 vs 动态语言
'''
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须
是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。
我们只需要保证传入的对象有一个run()方法就可以了：
'''
class Timer(object):
	def run(self):
		print('Start...')
run_twice(Timer())
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
#一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

#Python的“file-like object“就是一种鸭子类型。
#对真正的文件对象，它有一个read()方法，返回其内容。
#但是，许多对象，只要有read()方法，都被视为“file-like object“。
#许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，
#完全可以传入任何实现了read()方法的对象。







