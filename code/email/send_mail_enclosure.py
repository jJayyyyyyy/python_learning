#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#如果Email中要加上附件怎么办？
#带附件的邮件可以看做包含若干部分的邮件：
#文本和各个附件本身，
#所以，可以构造一个MIMEMultipart对象代表邮件本身，
#然后往里面加上一个MIMEText作为邮件正文，
#再继续往里面加上表示附件的MIMEBase对象即可

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
with open('/Users/steve/Downloads/p.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='p.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='p.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



'''
参考
https://docs.python.org/3.5/library/email-examples.html
发送附件的时候还要
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
否则会出现NameError
'''
