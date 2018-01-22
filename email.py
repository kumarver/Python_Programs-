import re
with open('test.txt','r+') as f:
	str1 = f.read()
	qa = re.findall(r'[\d\w\.]+\@[\d\w\.]+',str1)
	print qa
			
