str1 = 'Hello World'
d = {}
for i in str1:
	keys = d.keys()
	if i in keys:
		d[i] +=1
	else:
		d[i] = 1
del d[' ']
print d
