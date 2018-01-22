'''
def permute(seq):
	if not seq:
		yield seq
	else:
		for  i in range(len(seq)):
			rest = seq[:i]+seq[i+1:]
			for x in permute(rest):
				yield seq[i:i+1] + x

print list(permute('abcd'))

'''

def permute(str1):
	if not str1:
		yield str1
	else:
		for i in range(len(str1)):
			rest = str1[:i] + str1[i+1:]
			for x in permute(rest):
				yield str1[i:i+1] + x

print list(permute('abcd'))	
