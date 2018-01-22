def smart_divide(func):
	def inner(a,b):
		print 'I am going divide %s and %s'%(a,b)
		if b==0:
			print "Whoops! cannot divide"
			return 
		return func(a,b)
	return inner

@smart_divide
def divide(a,b):
	print a/b

divide(12,0)
