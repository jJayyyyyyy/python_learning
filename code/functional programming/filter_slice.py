#Python内建的filter()函数用于过滤序列
#和map()类似，filter()也接收一个函数和一个序列
#它把传入的函数依次作用于每个元素，根据返回值是True/False决定保留/丢弃该元素。

#例如，在一个list中，删掉偶数，只保留奇数，可以这么写
def is_Odd(n):
	return n%2==1
print(list(filter(is_Odd, [1, 2, 3, 4, 5, 6])))

#把一个序列中的空字符串删掉
def not_Empty(s):
	return s and s.strip()
print(list(filter(not_Empty, ['A', '', 'B', None, ' ', 'c'])))

#可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列
#所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list



#用filter求素数
#先构造一个从3开始的奇数序列：
def _odd_iter():
	n = 1
	while True:
		n = n+2
		yield n
#然后定义一个筛选函数
def _not_divisible(n):
	return lambda x: x % n > 0
#最后，定义一个生成器，不断返回下一个素数
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible, it)
for n in primes():
	if n < 20:
		print(n)
	else:
		break



#homework
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909
#利用filter()滤掉非回数
def is_palindrome(n):
	#得到字符串,比较正反顺序
	return str(n) == str(n)[::-1]

print(list(filter(is_palindrome, range(1,100))))


'''
#思路：参考使用切片slice，以及str(n)字符串化
n=12345
print(str(n)[0])
print(str(n)[-1])
#1 5
print(str(n))
#1 2 3 4 5
print(str(n)[::2])
#1 3 5
print(str(n)[::-1])
#5 4 3 2 1
'''