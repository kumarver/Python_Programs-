import thread
import time 
def test(power_of,limit,thread_n,delay):
	a = power_of
	print thread_n+':',a
	for i in range(limit):
#		time.sleep(delay)
		a = power_of**(power_of+i)
		if a < limit:
			print  '%s: %s'%(thread_n,a)

try:
	thread.start_new_thread(test,(2,20,'Thread-1',2))
	thread.start_new_thread(test,(3,20,'Thread-2',4))
except:
	print 'Unable to start thread'
while 1:
	pass
