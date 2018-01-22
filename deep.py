import copy
ls1 = [1,2,[3,5],4]
ls2 = copy.deepcopy(ls1)
print ls1
print ls2
ls2[2][0]=7
print 'After deep copy '
print ls2
print ls1
