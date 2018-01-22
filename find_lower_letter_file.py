with open('test.txt','r+') as f:
	count = 0
	data = f.read()
	for char in data:
		if char.islower():
			count += 1
print count
