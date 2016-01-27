#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#如果要把一个图片嵌入到邮件正文中怎么做？直接在HTML邮件中链接图片地址行不行？
#答案是，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。

#要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，
#然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
#如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。

#把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片：

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
msg.attach(MIMEText('<html><body><h1>Hello</h1>' + '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8'))
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
