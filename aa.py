'''
A0=dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print A0
A1=range(10)
print A1
A2=sorted([i for i in A1 if i in A0])
print A2
A3=sorted([A0[s] for s in A0])
print A3

A4=[i for i in A1 if i in A3]
print A4

#A5={i for i in A1 }
#print A5

A6=[[i,i*i] for i in A1]
print A6
'''
A1= [0,1,2,3,4,5,6,7,8,9]
#A2=sorted([i for i in A1 if i in A0])
#print A2
A0 = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
A2 = []
for i in A0:
	A2.append(A0[i])
print sorted(A2)
