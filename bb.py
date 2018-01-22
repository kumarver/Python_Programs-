'''
str1='Hello World'
ls = str1.split()
d = {}
for i in str1:
	keys = d.keys()
	if i in keys:
		d[i] += 1
	else:
		d[i]=1

print d
'''
str1='Hello World'
d = {}
for i in str1:
	if i != ' ':
		d[i]=str1.count(i)
print d.items()
