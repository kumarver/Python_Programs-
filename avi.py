ls = [0,1,2,3,4,5,6,7,8,9,10]
# new = [1,9,2,8,3,7,4,6,5]
new = []
for i in range(len(ls)):
	if ls == [] :
		break
	elif len(ls) == 1:
		new.append(ls[0])
		break
	else:
		new.append(min(ls))
		new.append(max(ls))
		ls.remove(min(ls))
		ls.remove(max(ls))

print new
