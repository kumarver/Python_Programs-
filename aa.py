def extendlist(val,list4=[]):
	list4.append(val)
	return list4

list1 = extendlist(10)
list2 = extendlist(123,[])
list3 = extendlist('a')

print 'list1 = %s'%list1
print 'list2 = %s'%list2
print 'list3 = %s'%list3 
