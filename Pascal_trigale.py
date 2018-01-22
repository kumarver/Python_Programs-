'''
def pascal_triangle(n):
   trow = [1]
   y = [0]
   count = n
   for x in range(max(n,0)):
      print ' '*(count-1), trow
      trow=[l+r for l,r in zip(trow+y, y+trow)]
      count -= 1
   return n>=1
pascal_triangle(6)
'''
def triangle(n):
	trow = [1]
	y = [0]
	count = n
	for x in range(max(n,0)):
		print ' '*(count),trow
		trow = [l+r for l,r in zip(trow+y,y+trow)]
		count -= 1
#	return n>=1

triangle(5)
