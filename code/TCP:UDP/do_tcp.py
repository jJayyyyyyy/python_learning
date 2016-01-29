'''
#Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
#而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。

#创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器
#创建Socket时，AF_INET指定使用IPv4协议，
#如果要用更先进的IPv6，就指定为AF_INET6。
#SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功
#但是还没有建立连接客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。
#新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址，
#但是怎么知道新浪服务器的端口号呢
#答案是作为服务器，提供什么样的服务，端口号就必须固定下来
#因为80端口是Web服务的标准端口。其他服务都有对应的标准端口号，
#例如SMTP服务是25端口，FTP服务是21端口，等等。
#端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))

#这儿和下面直接换成www.liaoxuefeng.com或者www.baidu.com还不行
#注意参数是一个tuple，包含地址和端口号。
#建立TCP连接后，我们就可以向新浪服务器发送请求，要求返回首页的内容：
s.send(b'Get / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')


#发送的文本格式必须符合HTTP标准，如果格式没问题，接下来就可以接收新浪服务器返回的数据了
buffer = []
while True:
	# 每次最多接收1k字节:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)
#接收数据时，调用recv(max)方法，一次最多接收指定的字节数，
#因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环

# 关闭连接:
s.close()

#接收到的数据包括HTTP头和网页本身，
#我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
	f.write(html)


'''


'''
另见 
do_tcp_test_server.py
do_tcp_test_client.py




小结

用TCP协议进行Socket编程在Python中十分简单，
对于客户端，要主动连接服务器的IP和指定端口，
对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。
通常，服务器程序会无限运行下去。

同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。
'''





#纯代码
#client
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80) )
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
	f.write(html)





