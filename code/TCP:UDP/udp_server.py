#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，
#就可以直接发数据包。但是，能不能到达就不知道了。
#它的优点是比TCP速度快

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9998))
#SOCK_DGRAM指定了这个Socket的类型是UDP
#绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据

print('Bind UDP on 9998')
while True:
	data, addr = s.recvfrom(1024)
	print('Received from %s: %s' % addr)
	s.sendto(b'Hello ' + data, addr)
	if not data:
		break
s.close()
#recvfrom()方法返回数据给data，客户端的地址与端口给addr
#注意这里省掉了多线程，因为这个例子很简单。

#客户端看udp_client.py


'''
#server参考
#server.py
#python2.7
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#host = '192.168.1.100'
host = '127.0.0.1'
port = 8000
s.bind((host, port))

#host = socket.gethostname() is the local-ip-address
#print '\nHost name is %s' % host

#or we can use the default addr, which is also the local-ip-addr
#	s.bind(('', 8000)) 

while True:
	data, addr = s.recvfrom(1024)
	if not data:
		print 'Received nothing! Client is offline!'
		break
	print 'Message:\t', data, '\tfrom\t', addr
s.close()
'''