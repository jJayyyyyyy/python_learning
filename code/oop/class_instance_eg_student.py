#面向对象最重要的概念就是类（Class）和实例（Instance）
class Student(object):
	
	def __init__(self, name, score):
		self.name = name
		self.score = score

bart = Student('Bart Simpson', 79)
print(bart)
print(bart.name, bart.score)

#和普通的函数相比，在类中定义的函数只有一点不同，
#就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数