num = int(raw_input('Enter the number to divdie:'))
divisorlist = []
for i in range(1,num+1):
	if num % i == 0:
		divisorlist.append(i)

print divisorlist
