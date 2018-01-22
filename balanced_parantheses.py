def isBalance(expr):
	import pdb;pdb.set_trace()
	opening = set('({[')
	match = set([('(',')'),('{','}'),('[',']')])
	stack = []
	if len(expr)%2 != 0:
		return False
	for char in expr:
		if char in opening:
			stack.append(char)
		else:
			if len(stack) == 0:
				return False
			lastChar = stack.pop()
			if (lastChar,char) not in match:
				return False
	return len(stack) == 0

print isBalance('({})')
			
