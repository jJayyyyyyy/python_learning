#Email的历史比Web还要久远，直到现在，Email也是互联网上应用非常广泛的服务。
#几乎所有的编程语言都支持发送和接收电子邮件

#假设我们自己的电子邮件地址是me@163.com，对方的电子邮件地址是friend@sina.com
#现在我们用Outlook或者Foxmail之类的软件写好邮件，填上对方的Email地址，
#点“发送”，电子邮件就发出去了。这些电子邮件软件被称为MUA：Mail User Agent 
#也即邮件用户代理

#Email从MUA发出去，不是直接到达对方电脑，而是发到MTA：
#Mail Transfer Agent——邮件传输代理，就是那些Email服务提供商，比如网易、新浪等等

#Email到达新浪的MTA后,新浪的MTA会把Email投递到邮件的最终目的地
#MDA：Mail Delivery Agent——邮件投递代理
#Email到达MDA后，就静静地躺在新浪的某个服务器上，
#存放在某个文件或特殊的数据库里，我们将这个长期保存邮件的地方称之为电子邮箱


#对方要取到邮件，必须通过MUA从MDA上把邮件取到自己的电脑上
#所以，一封电子邮件的旅程就是：
#发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人



#有了上述基本概念，要编写程序来发送和接收邮件，本质上就是：
#编写MUA把邮件发到MTA；
#编写MUA从MDA上收邮件。

#发邮件时，MUA和MTA使用的协议就是SMTP
#SMTP：Simple Mail Transfer Protocol，
#一个MTA到另一个MTA也是用SMTP协议。

#收邮件时，MUA和MDA使用的协议有两种：
#POP：Post Office Protocol，目前版本是3，俗称POP3；
#IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件
#还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱等等

#当然，客户端收发邮件的时候还要配置服务器地址以及验证用户口令



















