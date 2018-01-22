data_list=[1,3,2,9,4,6,7,8]
new_list=[]
while data_list:
	minimum = data_list[0]
	for x in data_list:
		 if x < minimum:
			minimum = x
	new_list.append(minimum)
	data_list.remove(minimum)

print new_list
