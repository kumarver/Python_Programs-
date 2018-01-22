import os
a = '.'
for dirpath,dirname,filename in os.walk(a):
	print 'Currecnt Path:',dirpath
	print 'Directry Names:',dirname
	print 'Filename:',filename

