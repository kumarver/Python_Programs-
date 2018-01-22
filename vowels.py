'''
def vowels(str1):
	count = 0 
	ls = []
	for i in str1:
		if i == 'a' :
			count +=1
			ls.append(i)	
		elif i == 'i':
			count +=1
			ls.append(i)
		elif i == 'e':
			count +=1
			ls.append(i)
		elif i == 'o':
			count +=1
			ls.append(i)
		elif i == 'u':
			count +=1
			ls.append(i)

	print count
	print ls
vowels('aloke')
'''
def vowels(str1= 'aalooku'):
	d = {}
	for i in str1:
		if i == 'a':
			d[i]=str1.count(i)
		elif i == 'o':
			d[i]=str1.count(i)
	print d

vowels()
