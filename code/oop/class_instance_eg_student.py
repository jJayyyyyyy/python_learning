#面向对象最重要的概念就是类（Class）和实例（Instance）
#每个对象都拥有相同的方法，但各自的数据可能不同

#类名通常是大写开头的单词
#紧接着是(object)，表示该类是从哪个类继承下来的
#通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
'''
class Student(object):
	
	def __init__(self, name, score):
		self.name = name
		self.score = score
#类起模板的作用，所以可以在创建实例的时候，把一些必须绑定的属性强制填写进去。
#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
#注意到__init__方法的第一个参数永远是self，表示创建的实例本身

bart = Student('Bart Simpson', 79)
print(bart)
print(bart.name, bart.score)
#和普通的函数相比，在类中定义的函数只有一点不同，
#就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
'''

'''
#可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。
#这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s: %s' % (self.name, self.score))
bart = Student('Bart Simpson', 79)
bart.print_score()
'''

#封装的另一个好处是可以给Student类增加新的方法，比如get_grade
#同样的，get_grade方法可以直接在实例变量上调用，不需要知道内部实现细节
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			print('A')
		elif self.score >= 60:
			print('B')
		else:
			print('C')

bart = Student('Bart Simpson', 79)
bart.print_score()
bart.get_grade()



#和静态语言不同，Python允许对实例变量绑定任何数据，
#也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，
#但拥有的变量名称都可能不同
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
#可以自由地给一个实例变量绑定属性
bart.age = 8
print(bart.age)

#print(lisa.age)
#会出错，因为只是bart自己绑定了name属性，lisa没有