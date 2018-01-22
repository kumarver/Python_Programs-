ls = [0,1,2,3,4,5,6,7,8,9,10]
print ls
ls1 = []
for i in range(len(ls)):
	if not ls:
		break
	elif len(ls) == 1:
		ls1.append(ls[0])
		break
	else:
		mins = min(ls)
		maxs = max(ls)
		ls1.append(maxs)
		ls1.append(mins)
		ls.remove(mins)
        	ls.remove(maxs)
print ls1
