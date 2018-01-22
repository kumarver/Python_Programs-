import commands
cmd = 'ls | grep bbb.py'
a = commands.getoutput(cmd)
print a
print type(a)
