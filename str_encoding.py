#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print ('rate is %2.1f %%' % r)




'''
#import math
name = 'ljj'
print ('Hello, %s!' % name)
print ('You have $%d now!' % 100000)
print ('% 03d-%03d' % (3,1))
print ('%.2f' % 3.145)
#print ('%.3f' % math.pi)
print ('%d %%.' % 7)
'''

'''
print ('ABC'.encode('ascii'))
print ('中文'.encode('utf-8'))
print (b'ABC'.decode('ascii'))
print (len('ABC'))
print (len(b'ABC'))
print (len('中文'.encode('utf-8')))
print ('中文测试正常')
'''

'''
print ('hello, 李')
print (ord('A'), ord('中'))
print (chr(66), chr(25991))
print ('\u4e2d\u6587')
x = b'ABC' 
# b表示 bytes数据类型,bytes以字节为单位，传输和储存
#python字符串类型是str，
#python 字符串使用的编码是Unicode
#Unicode表示的str可以通过encode()方法编码为指定的bytes
#把bytes变为str，用decode()方法
'''
