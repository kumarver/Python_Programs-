str1='abcb b'
str2 = ''
import string 

for i in str1:
	if i == 'd':
		str1 = string.replace(str1,'d','x')
	elif i == 'b':
		str1 = string.replace(str1,'b','y')
	elif i == 'c':
		str1 = string.replace(str1,'c','z')
print str1
