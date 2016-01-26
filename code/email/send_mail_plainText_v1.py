#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件
#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
#首先，我们来构造一个最简单的纯文本邮件
from email.mime.text import MIMEText
msg = MIMEText('Hello, sent by Python...', 'plain', 'utf-8')
#第一个参数就是邮件正文，第二个参数是MIME的subtype，
#传入'plain'表示纯文本，最终的MIME就是'text/plain'
#最后一定要用utf-8编码保证多语言兼容性
from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25)#SMTP默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

#出现 smtplib.SMTPDataError:
#查询了里面提到的网址，说是垃圾邮件不能发送……
#再查了网易的反垃圾邮件政策，里面写了一条：
#使用或包括无效的或伪造的邮件头
#我去……然后按照第二个示例，添加了邮件头，就收到邮件啦~











