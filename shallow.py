import copy
ls1 = [1,2,[3,5],4]
ls2 = copy.copy(ls1)
print 'Before the shallow copy',ls1
ls2[2][0]=7
print 'After chages in copyed list',ls2
print 'Original list',ls1
