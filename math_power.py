import math
def test(limit):
	print '2.0'
	for i in range(limit):
		if math.pow(2,2+i) < limit:
			print math.pow(2,2+i)

test(10)
