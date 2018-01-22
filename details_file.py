import re
with open('qa.txt','r') as f:
	a = f.readlines()
	for i in range(len(a)):
#		print a[i]
#		print type(i)
		if re.findall(r'^Alok',a[i]):
			print 'pass'
