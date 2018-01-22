import os
cmd = 'ifconfig eth0 | grep "inet addr"'
print os.system(cmd)

