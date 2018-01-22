import csv

with open('details.csv','r') as fr:
	csv_reader = csv.DictReader(fr)
	#print csv_reader
	for line in csv_reader:
		print line['email']

