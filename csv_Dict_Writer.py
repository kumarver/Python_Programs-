import csv

with open('details.csv','r') as fr:
	csv_reader = csv.DictReader(fr,delimiter = ',')
	with open('dict_details.csv','w') as fw:
		fieldnames = ['first','last','email','salary']
		csv_writer = csv.DictWriter(fw,fieldnames=fieldnames,delimiter=',')

#		csv_writer.writeheader()

		for line in csv_reader:
			csv_writer.writerow(line)

