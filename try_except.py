try:
	f = open('test.txt','r')
except IOError as e:
	print e

except Exception as e:
	print e

else:
	print f.read()
	f.close()

finally:
	print 'Executing Finally...'
