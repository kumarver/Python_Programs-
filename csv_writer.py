import csv

with open('details.csv', 'r') as fr:
	csv_reader = csv.reader(fr)
	with open('new_details.csv','w') as fw:
		csv_writer = csv.writer(fw,delimiter = ',')
		for line in csv_reader:
			csv_writer.writerow(line)
