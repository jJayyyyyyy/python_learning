* 题目所述“从A借助B移动到C”，这句的理解很关键

* 注意move(n, a, b, c)中的a, b, c，是抽象出来的参数，
其中a代表起点，b代表临时点，c代表终点，递归内部并不一定每次都和'A','B','C'对应

---

* 想明白以上注意点后，再理解代码就不会想不明白了  
<pre><code>
def move(n, a, b, c):
	if n==1:
		print(a, '-->', c)
		return
	move(n-1, a, c, b)
	move(1, a, b, c)
	move(n-1, b, a, c)
	move(3, 'A', 'B', 'C') 
</code></pre>

	其中，move(n-1, a, c, b)是把上面n-1个从起点经过临时点放到终点，并不一定是从'A'经过'C'再到'B'(比如第二层调用时就不是)  
	move(1, a, b, c)  
	move(n-1, b, a, c)  
	同理

*	因为在递归内部的参数并不一定每次都和'A','B','C'对应，a,b,c只是起点、临时点、终点的抽象。  
	不过还是容易混淆，所以最好起个有意义的名字作为参数名  
  
  	```
  	def move(n, start, temp, destination):
  		pass  
	```



