# [HTTP协议简介](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432011939547478fd5482deb47b08716557cc99764e0000)

在Web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让浏览器显示出来。

* HTML是一种用来定义网页的文本，会HTML，就可以编写网页

* HTTP是在网络上传输HTML的协议，用于浏览器和服务器间的通信


* Request Headers  浏览器发给服务器的请求

 > GET / HTTP/1.1 

 `GET`表示一个读取请求，将从服务器获得网页数据，

 `/`表示URL的路径，URL总是以`/`开头，`/`就表示首页，
 
 最后的HTTP/1.1指示采用的HTTP协议版本是1.1。目前HTTP协议的版本就是1.1，但是大部分服务器也支持1.0版本，主要区别在于1.1版本允许多个HTTP请求复用一个TCP连接，以加快传输速度。 

 > Host: www.douban.com

 表示请求的域名是`www.douban.com` 。如果一台服务器有多个网站，服务器就要通过`Host`来区分客户端浏览器到底请求的是哪个网站。
 
* Response Headers  显示服务器返回的响应数据

 HTTP响应分为`Header`和`Body`两部分(Body是可选项)
 
 Header
 > HTTP/1.1 200 OK

 200表示一个成功的响应，OK是说明，失败的响应有`404 Not Found`、`500 Internal Server Error`等等

 > Content-Type: text/html
 
 `Content-Type`指响应的内容，这里是`text/html`，表示HTML网页。
 注意浏览器是依靠`Content-Type`来判断响应的内容是网页还是图片，是视频还是音乐。浏览器并不靠`URL`来判断响应的内容，所以，即使URL是`http://example.com/abc.jpg`，它也不一定就是图片。

 HTTP响应的`Body`就是HTML源码，我们在菜单栏选择“视图”，“开发者”，“查看网页源码”就可以在浏览器中直接查看HTML源码
 
 当浏览器读取到新浪首页的HTML源码后，它会解析HTML，显示页面，然后，根据HTML里面的各种链接，再发送HTTP请求给新浪服务器，拿到相应的图片、视频、Flash、JavaScript脚本、CSS等各种资源，最终显示出一个完整的页面。所以我们在Network下面能看到很多额外的HTTP请求




> 本文档只为学习python/git/github/markdown所用，原文链接地址如下
> 
> [廖老师的教程地址](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432011939547478fd5482deb47b08716557cc99764e0000)