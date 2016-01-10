# -*- coding: utf-8 -*-

#使用递归函数的优点是逻辑简单清晰
#缺点是过深的调用会导致栈溢出

#阶乘
def fact(n):
	if n==1:
		return 1
	return n * fact(n-1)
print(fact(3))
#使用递归函数需要注意防止栈溢出。
#在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
#每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
#由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

#优化
#尾递归是指，在函数返回的时候，调用函数本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化
#使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact_pro(n):
	return fact_iter(n, 1)
def fact_iter(num, result):
	if num==1:
		return result
	return fact_iter(num-1, num*result)
print(fact_pro(5))
#知头知尾，就像循环
#比如 5!=5x4x3x2x1, 5要给定，1也要知道

#Haoni Tower汉诺塔
#参数说明: 从a借助b移动到c
def move(n, a, b, c):
	
	if n==1:
		print(a, '-->', c)
		return
	move(n-1, a, c, b)
	move(1, a, b, c)
	move(n-1, b, a, c)
move(3, 'A', 'B', 'C')
#算法：
#1: 若只有一个盘子，把它从a到c，写成print(a, '-->', c)
#2: 多个盘子，先把它上面的n-1个从a(起点)移动到b(中介)，然后把最后一个移动到c(终点)，然后把B的n-1个移动到c。



