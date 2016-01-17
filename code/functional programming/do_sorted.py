#sort 也是把方法作用在每一个元素身上

#sort a list
print(sorted([1, 3, 0, -12]))

#use key
print(sorted([10, -5, 3, 7, -2], key=abs))

#string
#use ASCII, 'A'=65, 'a'=97
print(sorted(['Bob', 'about', 'Zoo', 'Credit']))

print()
print(ord('A'))
print(chr(97))

#忽略大小写
print(sorted(['Bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#反向排序
print(sorted(['Bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
#从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁

#用sorted()排序的关键在于实现一个映射函数
#也就是赋给key的东西(abs, str.lower, ...)
#看练习就知道了


#练习
#假设我们用一组tuple表示学生名字和成绩：
#L=[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表，先按名字排序，再按成绩从高到低排序
L=[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sort_by_name(tuple):
	#t是tuple
	return tuple[0]
def sort_by_score(t):
	return t[1]


L2 = sorted(L, key=sort_by_name)
print(L2)
L3 = sorted(L, key=sort_by_score, reverse=1)
print(L3)



'''
解答
* t是参数名，起这个名字只是方便理解，这里理解为tuple，因为`L`这个`list`的每一个元素是一个`tuple`。不是tuple也能这样用啊(不信你试试
`L=[['Bob', 75], ['Adam', 92], ['Bart', 66], ['Lisa', 88]]`)
。`L[0]`不就是把`L`的第一个元素打出来嘛。。题中所给`L`的元素是`tuple`只是为了防止改动吧，你去看看之前的`使用list和tuple`这一节
 `不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。`


* 你要知道这篇教程还是在`高阶函数`这一节里面的，也就是说可以根据`MapReduce`以及`filter`来理解。
* 举个栗子，一开始廖老师也讲了
```
sorted([36, 5, -12, 9, -21], key=abs)
```
`key`指定的函数`abs`将作用于`list`的每一个元素上，
`key`指定的函数`abs`将作用于`list`的每一个元素上，
`key`指定的函数`abs`将作用于`list`的每一个元素上，
然后根据每个元素的大小或者字符的ASCII值排序

* 层主的代码是省略版的，完整的就是这样

```
L=[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sort_by_name(t):
	return t[0]
def sort_by_score(t):
	return t[1]
print(sorted(L, key=sort_by_name))
print(sorted(L, key=sort_by_score, reverse=1))
```
也就是首先把`sort_by_name`作用于`list`的每一个元素上，根据返回的结果`['B','A','B','L']`再来排序，不过有两个`'B'`, 那就要回去再做一次

* 反正最后得到的结果是
```
[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
```
```
[('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]
```
'''