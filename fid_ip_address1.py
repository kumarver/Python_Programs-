from subprocess import check_output
hostname = check_output(['hostname', '-I'])
print 'IP addresss:' + hostname + '\n'
