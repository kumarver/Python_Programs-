with open('test.txt', 'r+') as f:
	count = 0 
	data = f.read()
	print type(data)
	for char in data:
		print char
		if char.isupper():
			count += 1

print count
