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
