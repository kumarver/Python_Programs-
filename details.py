with open('empl.txt','r') as f:
	str1 = f.readlines()
	empl_name = []
	salary = []
	for i in str1:
		a = i.split(' ')[2]
		salary.append(a.strip())
		b = i.split(' ')[1]
		empl_name.append(b)
	qa = zip(salary,empl_name)
	print qa
	#print sorted(qa)
	qa1 = qa.sort(reverse=True)
	print qa

	
