'''
def smartdivison(func):
	def inner(a,b):
		print 'Going to divide %s and %s'%(a,b)
		if b == 0:
			print 'Whoops cannot divide via zero'
			return 
		return func(a,b)
	return inner

@smartdivison
def divide(a,b):
	print a/b

divide(12,0)
'''
def smart_divide(func):
	def inner(a,b):
		print 'Going to divide {0} via {1}'.format(a,b)
		if b == 0:
			print 'Whoops! can not divide via zero'
			return
		return func(a,b)
	return inner

@smart_divide
def divide(a,b):
	print a/b

divide(12,0)

