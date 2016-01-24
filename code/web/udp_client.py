#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#客户端使用UDP时，首先仍然创建基于UDP的Socket，
#然后，不需要调用connect()，直接通过sendto()给服务器发数据

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Mark', b'Tom', b'Sam']:
	s.sendto(data, ('127.0.0.1', 9998))
	print(s.recv(1024).decode('utf-8'))
s.close()


'''
#client参考
#client.py
#python2.7
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#host = '192.168.1.102'
host = '127.0.0.1'
port = 8000

while True:
	msg = raw_input()
	if not msg:
		break
	s.sendto(msg, (host, port))
s.close()
'''