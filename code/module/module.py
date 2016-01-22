#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#1.
#你也许还想到，如果不同的人编写的模块名相同怎么办？
#为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。

#举个例子，一个abc.py的文件就是一个名字叫abc的模块，
#一个xyz.py的文件就是一个名字叫xyz的模块。

#请注意，每一个包目录下面都会有一个__init__.py的文件，
#这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
#__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块


#2.使用模块
#以内建的sys模块为例

#任何模块代码的第一个字符串都被视为模块的文档注释
' a test module'

#使用__author__变量把作者写进去
__author__ = 'Michael'

import sys
#导入sys模块后，我们就有了变量sys指向该模块，
#利用sys这个变量，就可以访问sys模块的所有功能

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello, world!')
	elif len(args) == 2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')

if __name__ == '__main__':
	test()

#当我们在命令行运行hello模块文件时，
#Python解释器把一个特殊变量__name__置为__main__，
#而如果在其他地方导入该hello模块时，if判断将失败，
#因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
#最常见的就是运行测试。

#命令行看效果
'''
$ python3 hello.py
Hello, world!
$ python hello.py Michael
Hello, Michael!
'''

