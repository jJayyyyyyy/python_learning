#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



'''
仔细观察send_mail_v1.py运行后的结果(如果能发送，也即不被判断为垃圾邮件)，
发现如下问题：

邮件没有主题；
收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
明明收到了邮件，却提示不在收件人中。
这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，
而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到
MIMEText中，才是一封完整的邮件
由此得到send_mail_v2.py
'''

'''
我们编写了一个函数_format_addr()来格式化一个邮件地址。
注意不能简单地传入name <addr@example.com>，
因为如果包含中文，需要通过Header对象进行编码。

msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。

再发送一遍邮件，就可以在收件人邮箱中看到正确的标题、发件人和收件人


你看到的收件人的名字很可能不是我们传入的管理员，
因为很多邮件服务商在显示邮件时，会把收件人名字自动替换为用户注册的名字，
但是其他收件人名字的显示不受影响。


如果我们查看Email的原始内容，可以看到如下经过编码的邮件头：

From: =?utf-8?b?UHl0aG9u54ix5aW96ICF?= <xxxxxx@163.com>
To: =?utf-8?b?566h55CG5ZGY?= <xxxxxx@qq.com>
Subject: =?utf-8?b?5p2l6IeqU01UUOeahOmXruWAmeKApuKApg==?=
这就是经过Header对象编码的文本，包含utf-8编码信息和Base64编码的文本。
如果我们自己来手动构造这样的编码文本，显然比较复杂
'''








