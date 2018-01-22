def reverseString(str1):
	new_str = ''
	ls = len(str1)
	while ls:
		ls -=1
		new_str +=str1[ls]
	return new_str

print reverseString('alok')


str2 = 'kumar'
print ''.join(reversed(str2))

str3 = 'Verma'	
print str3[::-1]
