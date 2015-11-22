## 工业项目设计学习第一步，熟悉开发工具

[Qt学习论坛](http://bbs.qter.org/)，东西多，但也杂  
[emouse的博客](http://www.cnblogs.com/emouse/category/449213.html)，以前学习STM32开发环境搭建时也是参考这位博主的

更多详细的步骤在上面都能找到，今天先不写，等明天把硬件设备全领了，然后向老师和师兄明确需求了再写。  

### 这里补充点其他的

## 在Terminal中直接输入命令就能打开QtCreator， i.e.
```bash
~$ qtcreator
```
就可以打开`Qt Creator`了。

想完成这个功能的原因是，一般在Linux下打命令比较方便，而师兄给下来的这个环境(已经打包成虚拟机，配置好了开发环境)，需要自己找到那个目录，一开始费了我好大劲才找到。。

如果可以像进入python的交互环境一样，直接不管在哪个目录只要来个
```bash
~$ python
```
那多省事~

OK废话少说。

## 步骤：  

### 1.在Terminal下直接输入命令就能打开QtCreator
* qtcreator所在原始目录是  
`/usr/local/QtCreator-2.8.1/bin/`  

* 首先在`/usr/bin/`目录下创建一个启动脚本`qtcreator`  
```bash
~$ sudo vi /usr/bin/qtcreator
```  
* 里面的内容  
```shell
#!/bin/sh
export QT_HOME=/usr/local/QtCreator-2.8.1/bin/
$QT_HOME/qtcreator $*
```
第一行是一个特殊的注释，和.py文件开头加个`#!/usr/bin/env python3`一样的作用。第2行是添加原始路径，第三行添加启动程序。  
然后给它执行权限
```bash
/usr/bin$ sudo chmod a+x qtcreator
```
然后在terminal敲个`qtc`，再tab一下，就能出现qtcreator了，第一步完成

### 2.添加桌面快捷方式  
如果还想添加桌面快捷方式，也不难。  

* 进入`/usr/share/applications/`，然后新建一个`qtcreator.desktop`
```bash
~$ sudo vi /usr/share/applications/
```  

* 进入编辑模式，写入以下内容，然后保存退出  
```bash
[Desktop Entry]
Type=Application
Name=qtcreator
Comment=QtCreator
Exec=/usr/local/QtCreator-2.8.1/bin/qtcreator
Terminal=false
Categories=Development;IDE;C++;
```

* 完成之后会在`/usr/share/applications/`目录下生成一个`qtcreator`，右键把它`Copy to` `Desktop`就好了~

<br/><br/>

我不会说我刚刚发现原来是有一个快捷方式的，而且有图标0.0不像我这个辣么丑。。不过自己动手做一做也不错~

<br/><br/><br/><br/>
## 参考
参考中是对Eclipse进行设置，Qt可以进行类似配置  
[参考1：在Terminal下直接输入命令就能打开QtCreator](http://www.cnblogs.com/lanxuezaipiao/p/3325628.html)  
[参考2：添加桌面快捷方式](http://www.2cto.com/os/201504/389987.html)  


