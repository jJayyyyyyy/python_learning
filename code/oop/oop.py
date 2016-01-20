'''
面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
为了简化程序设计，面向过程把函数继续切分为子函数，
即把大块函数通过切割成小块函数来降低系统的复杂度。

而面向对象的程序设计把计算机程序视为一组对象的集合，
而每个对象都可以接收其他对象发过来的消息，并处理这些消息，
计算机程序的执行就是一系列消息在各个对象之间传递。

在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。
自定义的对象数据类型就是面向对象中的类（Class）的概念。
'''
#面向过程
std1 = {'name':'Michael', 'score':98}
std2 = {'name':'Bob', 'score':81}
def print_score(std):
	print('%s: %s' % (std['name'], std['score']))

#面向对象
#如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，
#而是Student这种数据类型应该被视为一个对象，
#这个对象拥有name和score这两个属性（Property）
#如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，
#然后给对象发一个print_score消息，让对象自己把自己的数据打印出来。
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))
#给对象发消息实际上就是调用对象对应的关联函数，称为对象的方法（Method）
#面向对象的程序写出来就像这样
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

#面向对象的设计思想是抽象出Class，根据Class创建Instance

#OOP的抽象程度比函数要高，因为一个Class既包含数据，又包含操作数据的方法
#数据封装、继承和多态是面向对象的三大特点


