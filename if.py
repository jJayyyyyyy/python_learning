# -*- coding: utf-8 -*-

#1.
age = 3
if age >= 18:
	print('your age is', age)
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')

#2.
birthYear = input('birthYear: ')
if birthYear<2000:
	print('before 00')
else:
	print("after 00")



'''
h = input('Please input your height(m): ')
w = input('Please input your weight(kg): ')
height = float(h)
weight = float(w)

indexBMI = weight/height/height

print ('%0.2f' % indexBMI)
'''