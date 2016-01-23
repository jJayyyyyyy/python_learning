#由于Python是动态语言，根据类创建的实例可以任意绑定属性
#或者通过self变量，或者通过实例变量。
class Student(object):
	def __init__(self, name):
		self.name = name

s = Student('Bob')
s.score = 90
print(s.name, s.score)
print()

#但是，如果Student类本身需要绑定一个属性呢？
#可以直接在class中定义属性，这种属性是类属性，归Student类所有
class Student(object):
	name = 'Stu'

#当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下
s = Student()
print(s.name)
print(Student.name)
s.name = 'Bob'
print(s.name)
print(Student.name)
print()
del s.name
print(s.name)



'''
从上面的例子可以看出，在编写程序的时候，
千万不要把实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，
访问到的将是类属性。
'''
