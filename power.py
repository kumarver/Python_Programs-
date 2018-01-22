def test(limit):
	qa = 2
	j = 2
	print j
	for i in range(limit):
		j = qa**(2+i)  
		if j <= limit:
			print j
test(110)
