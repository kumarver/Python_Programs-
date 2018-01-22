import csv

with open('details.csv','r') as f:
	csv_reader = csv.reader(f)
	next(csv_reader)
	d = {}
	for line in csv_reader:
		d[line[0]] = line[3]
	d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])
	print d
	print d_sorted_by_value
'''
with open('details.txt','r') as fr:
	ls = fr.readlines()
	salary = []
	name = []
	for lines in ls:
		n = lines.split()[0]
		name.append(n)
		s = lines.split()[3]
		salary.append(s)
	d = zip(salary,name)
	qa = sorted(d)
	print qa
'''
