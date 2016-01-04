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
