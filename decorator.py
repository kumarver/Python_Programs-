def smart_divide(func):
	def inner(a,b):
		print 'Going to divide {0} via {1}'.format(a,b)
		if b==0:
			print 'Whoops! Can not divide by zero'
			return 
		return func(a,b)
	return inner

@smart_divide
def divide(a,b):
        print a/b

divide(4,0)
