**[参考教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320122322996f770fbf5da84ead84a1731e1dde129f000)**

### HTML

* 一个简单的例子

 ```html
	<html>
	<head>
		<title>Hello</title>
	</head>
	<body>
  		<h1>Hello, world!</h1>
  	</body>
	</html>
 ```

* HTML文档就是一系列的Tag组成，最外层的Tag是<html>。规范的HTML也包含<head>...</head>和<body>...</body>（注意不要和HTTP的Header、Body搞混了），由于HTML是富文档模型，所以，还有一系列的Tag用来表示链接、图片、表格、表单等等。

### CSS

* `CSS` is short for `Cascading Style Sheets`(层叠样式表) 
 
* CSS用来控制HTML里的所有元素如何展现，比如，给标题元素<h1>加一个样式，变成48号字体，灰色，带阴影：

 ```html
	<html>
	<head>
		<title>Hello</title>
		<style>
			h1{
				color: #333333;
				font-size: 48px;
				text-shadow: 3px 3px 3px #666666;
			}
		</style>
	</head>
	<body>
		<h1>Hello, world!</h1>
	</body>
	</html>
```

## 小结
* 如果要学习Web开发，首先要对HTML、CSS和JavaScript作一定的了解。

* HTML定义了页面的内容，CSS来控制页面元素的样式，而JavaScript负责页面的交互逻辑。

* 当我们用Python或者其他语言开发Web应用时，我们就是要在服务器端动态创建出HTML，这样，浏览器就会向不同的用户显示出不同的Web页面。

* 在线学习网站w3schools
[http://www.w3schools.com/](http://www.w3schools.com/)

 以及一个对应的中文版本：
[http://www.w3school.com.cn/](http://www.w3school.com.cn/)