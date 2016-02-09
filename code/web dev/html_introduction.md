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