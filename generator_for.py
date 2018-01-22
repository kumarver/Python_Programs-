def fib(limit):
	a ,b = 0,1
	while a < limit:
		yield a
		a, b = b , a+b

for a in fib(5):
	print a
