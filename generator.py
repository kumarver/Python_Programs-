def my_gen():
	n =1 
	print 'This is first '
	yield n
	
	n +=1
	print 'This is second'
	yield n

	n +=1
	print 'This is third'
	yield n

a = my_gen()
next(a)
next(a)
next(a)
next(a)
