'''
def print_direct_file(spath):
	import os
	for schild in os.listdir(spath):
		schildpath = os.path.join(spath,schild)
		if os.path.isdir(schildpath):
			print_direct_file(schildpath)
		else:
			print schildpath
print_direct_file('.')
'''

def dirct(first):
	import os 
	for second in os.listdir(first):
		third = os.path.join(first,second)
		if os.path.isdir(third):
			dirct(third)
		else:
			print third

dirct('.')
