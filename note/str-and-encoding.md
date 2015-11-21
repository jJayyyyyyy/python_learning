# 字符串和编码
## 1.编码
* 内存中，统一使用Unicode编码。
* 需要保存到硬盘或者传输时，就转换为UTF-8编码
* 记事本编辑的时候，从文件读取的UTF-8被转换为Unicode到内存

<div align='center'>
<img src=http://www.liaoxuefeng.com/files/attachments/001387245992536e2ba28125cf04f5c8985dbc94a02245e000/0 width='240' />
</div>

## 2.Python的字符串编码
* Python3中，字符串以Unicode编码，即支持多语言
* `>>> ord('A')`  
  `65`  
  `>>> ord('中')`  
  `20013`  
 得到字符的十进制整数编码表示<br/>
* `>>> chr(66)`  
  `B`  
  `>>> chr(25991)`  
  `'文'`  
  把编码转换为数字<br/>
* Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes.<br/><br/>
以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
`>>>'ABC'.encode('ascii')`  
`b'ABC'`   
* 为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。  

 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
`#!#!/usr/local/bin/python3`
`# -*- coding: utf-8 -*-`  
其中第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。  

* 更多的细节参考[廖老师的博客](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000#0) 

## 格式化输出字符串
* 同C语言，用%  
`>>> 'Hello, %s!' % 'world'`  
`'Hello, world!'`

* 更多细节参考同上


<br/>