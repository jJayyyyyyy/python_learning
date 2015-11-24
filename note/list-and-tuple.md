## list，列表
list(类似数组)，python的一种数据类型，可以随时添加和删除元素  

`>>> students = ['Micheal', 'Bob', 'Tracy']`  
`['Micheal', 'Bob', 'Tracy']`  
这里变量students就是一个list

* 获得长度  
`>>> len(students)`  
`3`

* 索引  
`>>> students[0]`  
`'Micheal'` #正向  
`>>> students[-1]`  
`'Tracy'` #反向

* 添加到末尾  
`>>> students.append('Adam')`  
`>>> students`  
`['Micheal', 'Bob', 'Tracy', 'Adam']`

* 插入到Index后面  
`>>> students.insert(1, 'Jack')`  
`>>> students`
`['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']`

* 删除Index位置  
`>>> students.pop(1)`  
`Jack`  
`>>> students`
`['Michael', 'Bob', 'Tracy', 'Adam']`  
 pop()方法参数为空时，默认删除最后一个  
`>>> students.pop()`  
`>>> students`
`['Michael', 'Bob', 'Tracy']` 

* 替换Index  
`>>> students[1] = 'Sarah'`  
`>>> students`  
`['Micheal', 'Tracy']`

* list的元素类型可以不同  
`>>> L = ['apple', 123, True]`  
元素可以是另外一个list  
`>>> lang = ['python', 'java', ['php', 'asp']]`  
`>>> len(lang)`  
`3` 一共三个元素  
这样看来，把list比作数组可是小看它了，应该像是结构体数组

## tuple，元组
* 与list相似，但是tuple一旦初始化便不能再修改，也即没有append(), insert()这样的方法。  
  注意: 这里的不变，指的是tuple指向(的内存地址)不变，不管内存里的内存是否可改。[参考](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316724772904521142196b74a3f8abf93d8e97c6ee6000)

* 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。  

* tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来。  
* 定义 ≠ 初始化，定义是声明，可以先定义有多少个元素，再对其初始化  
<br/>定义:  
`>>> t=(3,)` 定义一个有3个元素的tuple  
`>>> t`  
`(3,)`  
<br/>初始化:  
`>>> t=('a', 'b', 'c')`  
`>>> t`  
`('a', 'b', 'c')`  

* 

<br/>
<br/>
<br/>
<br/>
