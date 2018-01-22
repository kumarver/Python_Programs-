a = raw_input('Enter a number:')
b = raw_input('Enter second number:')
try:
	z = int(a)/ int(b)
except ZeroDivisionError:
	print 'Divide by zero exception'

except TypeError:
	print 'String and int we can not divide'

else:
	print 'Divide {0}/{1}: {2}'.format(a,b,z)


