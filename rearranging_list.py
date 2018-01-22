def rearrange(ls,n):
	temp = n*[None]
	small,large=0,n-1
	flag = True
	for  i in range(n):
		if flag is True:
			temp[i] = ls[large]
			large -= 1
		else:
			temp[i] = ls[small]
			small += 1
		flag = bool(1-flag)
	print temp

ls = [1,2,3,4,5,6,7]
n = len(ls)
rearrange(ls,n)
