with open('test.txt','r') as rf:
	with open('test1.txt', 'r') as rf1:
		with open('test2.txt', 'r+') as wr:
			data = rf.readlines()
			data1 = rf1.readlines()
			data2 = wr.readlines()	
			print data2
			l1 = len(data)
			l2 = len(data1)
			l3 = len(data2)
			mx = max(l1,l2,l3)
			wr.seek(0,0)
			i = 1
			while i <= mx:
				if i <= l1-1:
					wr.write(data[i])
				elif i <=l2:
					wr.write(data1[i])
				elif i <=l3:
					print '-----'
					wr.write(data2[i])

				i +=1
