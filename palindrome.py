wrd = str(raw_input('Please enter the word:'))
str1 = wrd[::-1]
if wrd == str1:
	print 'This word is palindrome'
else:
	print 'Thos word is not palindrome'
