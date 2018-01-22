str1='Hellollo'
'''
my_list=[]
my_list.append(str1[0])
for i in range(1,len(str1)):
	if str1[i] in my_list:
		print str1[i]
	else:
		my_list.append(str1[i])
'''
d = {}
for i in range(len(str1)-1):
	if str1[i] == str1[i+1]:
		d[i] = 1
#		d.append(str1[i])
#		d.append(str1[i+1])
print d
	
